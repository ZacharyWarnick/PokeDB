"""Abstracts database interaction away from API endpoint definitions.

Note:
    Each method in this module must be run from within a flask app context.
    Methods integrate flask-specific functionality such as producing a 404
    error when an invalid query is executed (e.g. by an invalid URL).
"""

from collections import defaultdict
from sqlalchemy import func, or_
from models import db, Pokemon, Evolution, Type

ITEMS_PER_PAGE = 16
ORDER_ASCENDING = 'ASC'
ORDER_DESCENDING = 'DESC'


def query_pokemon_list(sort_key, sort_order, page_number,
                       item_count=ITEMS_PER_PAGE):
    """Queries for a list of Pokémon.

    Sort Keys:
        id: The ID of the Pokémon.
        name: The name of the Pokémon.
        gen: The generation that the Pokémon was introduced.
        color: The average base stat sum for the type.
        type: A heuristic value measuring a type's general advantage in battle.

    Args:
        sort_key: The key used to sort results.
        sort_order: Ascending (ASC) or descending (DESC).
        page_number: The page index for pagination, must be >= 1.
        item_count: The number of items per page.

    Returns:
        A list of dictionaries describing each Pokémon.
    """
    sort_params = (sort_key, sort_order)
    default_sort = Pokemon.id.asc()
    sort = {
        ('id', ORDER_DESCENDING): (Pokemon.id.desc(),),
        ('name', ORDER_ASCENDING): (Pokemon.name.asc(),),
        ('name', ORDER_DESCENDING): (Pokemon.name.desc(),),
        ('gen', ORDER_ASCENDING): (
            Pokemon.since_gen.asc(), Pokemon.name.asc()),
        ('gen', ORDER_DESCENDING): (
            Pokemon.since_gen.desc(), Pokemon.name.asc()),
        ('color', ORDER_ASCENDING): (Pokemon.color.asc(), Pokemon.id.asc()),
        ('color', ORDER_DESCENDING): (Pokemon.color.desc(), Pokemon.id.asc()),
        ('type', ORDER_ASCENDING): (
            Pokemon.first_type_id.asc(), Pokemon.id.asc()),
        ('type', ORDER_DESCENDING): (
            Pokemon.first_type_id.desc(), Pokemon.id.asc()),
        }.get(sort_params, default_sort)

    query = Pokemon.query.order_by(*sort)
    items = query.paginate(page_number, item_count).items
    return [it.to_dict() for it in items]


def query_pokemon(pokemon):
    """Queries for detailed information on a specific Pokémon.

    Args:
        pokemon: An integer or string identifier for a Pokémon.

    Returns:
        A dictionary describing the Pokémon.
    """
    filter_key = 'identifier' if isinstance(pokemon, str) else 'id'
    filter_args = {filter_key: pokemon}
    item = Pokemon.query.filter_by(**filter_args).first_or_404()
    return item.to_dict(show=Pokemon.EXTRA_FIELDS)


def _query_sorted_evolutions(sort_key, sort_order, page_number, item_count):
    """A helper query to sorting which groups evolution_chain_id.

    A second query is required to obtains the specific evolution items.
    This query serves only to determine which items should be selected.

    Returns:
        A dictionary mapping chain IDs to fields used in the sorting process.
    """
    sort_params = (sort_key, sort_order)
    default_sort = Evolution.evolution_chain_id.asc()

    chain_count = func.count(
        func.distinct(Evolution.pokemon_id)
        ).label('chain_count')
    diff_sum = func.sum(Evolution.difficulty).label('difficulty')
    max_level = func.max(Evolution.level).label('max_level')
    base_pokemon = func.min(
        Evolution.evolves_from_pokemon_id).label('base_pokemon')

    sort = {
        ('chain', ORDER_DESCENDING): Evolution.evolution_chain_id.desc(),
        ('diff', ORDER_ASCENDING): diff_sum.asc(),
        ('diff', ORDER_DESCENDING): diff_sum.desc(),
        ('count', ORDER_ASCENDING): chain_count.asc(),
        ('count', ORDER_DESCENDING): chain_count.desc(),
        ('level', ORDER_ASCENDING): chain_count.asc(),
        ('level', ORDER_DESCENDING): chain_count.desc(),
        ('base', ORDER_ASCENDING): base_pokemon.asc(),
        ('base', ORDER_DESCENDING): base_pokemon.desc()
        }.get(sort_params, default_sort)

    # Get ordered chains of evolutions.
    join_rel = or_(
        Pokemon.id == Evolution.evolves_from_pokemon_id,
        Pokemon.id == Evolution.pokemon_id)

    entities = [
        Evolution.evolution_chain_id, base_pokemon, chain_count, diff_sum,
        max_level]

    query = db.session.query(Evolution).with_entities(*entities)
    query = query.join(Pokemon, join_rel)
    query = query.group_by(Evolution.evolution_chain_id)
    query = query.order_by(sort)

    result = query.paginate(page_number, item_count).items
    chain_details = {}
    for row in result:
        chain_details[row.evolution_chain_id] = {
            'difficulty': row.difficulty,
            'chain_count': row.chain_count,
            'base_pokemon': row.base_pokemon,
            'max_level': row.max_level
            }

    return chain_details


def query_evolution_list(sort_key, sort_order, page_number,
                         item_count=ITEMS_PER_PAGE):
    """Queries for details about various evolution chains.

    Sort Keys:
        chain: The ID of the evolution chain.
        diff: The total difficulty required to fully evolve a chain.
        level: The maximum level required by an evolution chain.
        base: The ID of the earliest-stage Pokémon in the chain.
        count: The number of possible stages of evolution in the chain.

    Note:
        Each evolution stage is indexed in the JSON by the identifier of the
        Pokémon which results from the evolution. For example, if you wanted to
        get the information for bulbasaur from the bulbasaur to ivysaur stage,
        it would be indexed as: `item['ivysaur']['evolves_from']`.

    Args:
        sort_key: The key used to sort results.
        sort_order: Ascending (ASC) or descending (DESC).
        page_number: The page index for pagination, must be >= 1.
        item_count: The number of items per page.

    Returns:
        A list of dictionaries, each containing values for the sortable
        attributes of a chain, as well as one stage for each evolution from one
        Pokémon to another. No details for the method of evolution are present.
    """
    chain_details = _query_sorted_evolutions(
        sort_key, sort_order, page_number, item_count)
    valid_chains = list(chain_details.keys())
    selection_filter = Evolution.evolution_chain_id.in_(valid_chains)
    rows = db.session.query(Evolution).filter(selection_filter).all()

    data = {}
    for row in rows:
        r_id = row.evolution_chain_id
        stage_key = row.pokemon.identifier  # Must be str for JSON conversion.
        chain_info = {
            'id': r_id,
            stage_key: row.to_dict()}

        if r_id not in data:
            # Copy over the chain details, once per chain.
            for k, v in chain_details[r_id].items():
                chain_info[k] = v

            # Create the entry for the chain in the data dict.
            data[r_id] = chain_info
        else:
            data[r_id].update(chain_info)

    s_key = {
        'chain': 'evolution_chain_id',
        'diff': 'difficulty',
        'count': 'chain_count',
        'base': 'base_pokemon',
        'level': 'max_level'
        }.get(sort_key, 'evolution_chain_id')

    def key(it): return it[s_key] if s_key in it else it['id']

    is_reverse = (sort_order == ORDER_DESCENDING)
    return sorted(data.values(), key=key, reverse=is_reverse)


def query_evolution(chain_id):
    """Obtains detailed information for a specific evolution chain.

    Args:
        chain_id: The evolution chain ID to query.

    Returns:
        A dictionary containing a list for each evolution to a given Pokémon.
        One Pokémon may evolve by mutiple methods, so each element in the list
        is a nested list containing each way the Pokémon may evolve.
    """
    selection_filter = Evolution.evolution_chain_id == chain_id

    # An evolution chain is composed of many evolution stages.
    # Every stage must be queried and then used to build the overall chain.
    rows = db.session.query(Evolution).filter(selection_filter).all()

    stages = defaultdict(list)
    for row in rows:
        dict_entry = row.to_dict(show=Evolution.EXTRA_FIELDS)
        stages[row.pokemon_id].append(dict_entry)

    sort_order = {}
    for stage in stages.values():
        print(stage[0])
        poke_id = stage[0]['pokemon']['id']

        pre_evolution = stage[0]['evolves_from']
        for i in range(5):
            # No Pokémon in the database should loop more than 2 times.
            # This guarantees that erroneous data won't cause an infinite loop.
            if pre_evolution is None:
                sort_order[poke_id] = i
                break

            pre_evolution = pre_evolution.get('evolves_from', None)

    def key(stage): return sort_order[stage[0]['pokemon']['id']]

    return sorted(stages.values(), key=key)


def query_type_list(sort_key, sort_order, page_number,
                    item_count=ITEMS_PER_PAGE):
    """Queries for a list of types.

    Sort Keys:
        id: The ID of the type.
        name: The name of the type.
        count: The number of Pokémon with the type.
        stats: The average base stat sum for the type.
        adv: A heuristic value measuring a type's general advantage in battle.

    Args:
        sort_key: The key used to sort results.
        sort_order: Ascending (ASC) or descending (DESC).
        page_number: The page index for pagination, must be >= 1.
        item_count: The number of items per page.

    Returns:
        A list of dictionaries describing each type.
    """
    sort_params = (sort_key, sort_order)
    default_sort = Type.id.asc()
    sort = {
        ('id', ORDER_DESCENDING): Type.id.desc(),
        ('name', ORDER_ASCENDING): Type.name.asc(),
        ('name', ORDER_DESCENDING): Type.name.desc(),
        ('count', ORDER_ASCENDING): Type.pokemon_count.asc(),
        ('count', ORDER_DESCENDING): Type.pokemon_count.desc(),
        ('stats', ORDER_ASCENDING): Type.stat_average.asc(),
        ('stats', ORDER_DESCENDING): Type.stat_average.desc(),
        ('adv', ORDER_ASCENDING): Type.relative_advantage.asc(),
        ('adv', ORDER_DESCENDING): Type.relative_advantage.desc()
        }.get(sort_params, default_sort)

    query = Type.query.order_by(sort)
    items = query.paginate(page_number, item_count).items
    return [it.to_dict() for it in items]


def query_type(a_type):
    """Queries data for a type by ID or identifier.

    Args:
        a_type: A type identifier ('normal') or ID (1).

    Returns:
        A dictionary describing the type.
    """
    filter_key = 'identifier' if isinstance(a_type, str) else 'id'
    filter_args = {filter_key: a_type}
    query = Type.query.filter_by(**filter_args)
    item = query.first_or_404()
    result = item.to_dict(show=Type.EXTRA_FIELDS)
    return result
