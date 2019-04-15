"""Abstracts database interaction away from API endpoint definitions.

Note:
    Each method in this module must be run from within a flask app context.
    Methods integrate flask-specific functionality such as producing a 404
    error when an invalid query is executed (e.g. by an invalid URL).
"""

from collections import defaultdict
from sqlalchemy import func, or_, not_
from models import db, Pokemon, Evolution, Type

ITEMS_PER_PAGE = 16
SEARCH_LIMIT = 5
ALL_MODELS = 'pokemon,type'

ASCENDING = 'ASC'
DESCENDING = 'DESC'


def to_dict(items, extra_cols):
    return [it.to_dict(show=extra_cols) for it in items]


def _read_pager_items(pager):  # pragma: no cover
    if (pager.items and not hasattr(pager.items[0], 'to_dict')):
        raise AttributeError('Pager items must have a `to_dict` method.')

    return [it.to_dict() for it in pager.items]


def _pager(pager, data=None):
    """Constructs a pager dictionary which wraps paged results.

    Note:
        The data object must have a false-y value or be a list of dictionaries.
        If the data object is false-y, then the items from the pager must have
        a function named `to_dict` which will be used to convert the pager
        items into a list of dictionaries.

    Args:
        pager: A SQLAlchemy pager object.
        data (optional): A list of items to return as the paged data.

    Returns:
        A dictionary containing several fields that detail the page state along
        with a data field which points to the page items.
    """
    data = data or _read_pager_items(pager)
    return {
        'current_page': pager.page,
        'page_count': pager.pages,
        'has_prev': pager.has_prev,
        'has_next': pager.has_next,
        'per_page': pager.per_page,
        'data': data
        }


def _sort_evolution_stages(stages):
    sort_order = {}
    for stage in stages:
        item = stage[0] if isinstance(stage, list) else stage
        poke_id = item['pokemon']['id']

        pre_evolution = item['evolves_from']
        for i in range(5):  # pragma: no branch
            # No Pokémon in the database should loop more than 2 times.
            # This guarantees that erroneous data won't cause an infinite loop.
            if pre_evolution is None:
                sort_order[poke_id] = i
                break

            pre_evolution = pre_evolution.get('evolves_from', None)

    def key(stage):
        item = stage[0] if isinstance(stage, list) else stage
        return sort_order[item['pokemon']['id']]

    return sorted(stages, key=key)


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
    is_descending = (sort_order == DESCENDING)
    default_sort = (Pokemon.id.desc() if is_descending else Pokemon.id.asc(),)

    sort = {
        ('id', DESCENDING): (Pokemon.id.desc(),),
        ('name', ASCENDING): (Pokemon.name.asc(),),
        ('name', DESCENDING): (Pokemon.name.desc(),),
        ('gen', ASCENDING): (
            Pokemon.since_gen.asc(), Pokemon.identifier.asc()),
        ('gen', DESCENDING): (
            Pokemon.since_gen.desc(), Pokemon.identifier.desc()),
        ('color', ASCENDING): (Pokemon.color.asc(), Pokemon.id.asc()),
        ('color', DESCENDING): (Pokemon.color.desc(), Pokemon.id.desc()),
        ('type', ASCENDING): (Pokemon.first_type_id.asc(), Pokemon.id.asc()),
        ('type', DESCENDING): (Pokemon.first_type_id.desc(), Pokemon.id.desc())
        }.get(sort_params, default_sort)

    query = Pokemon.query.order_by(*sort)
    pager = query.paginate(page_number, item_count)
    return _pager(pager)


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
        A 2-tuple containing the source pager object and a dictionary
        containing dictionaries for each evolution chain which store the
        sortable attributes for each entry.
    """
    sort_params = (sort_key, sort_order)
    is_descending = (sort_order == DESCENDING)
    default_sort = (Evolution.evolution_chain_id.desc()
                    if is_descending else Evolution.evolution_chain_id.asc())

    chain_count = func.count(
        func.distinct(Evolution.pokemon_id)
        ).label('chain_count')
    diff_sum = func.sum(Evolution.difficulty).label('difficulty')
    max_level = func.max(Evolution.level).label('max_level')
    base_pokemon = func.min(
        Evolution.evolves_from_pokemon_id).label('base_pokemon')

    sort = {
        ('chain', DESCENDING): Evolution.evolution_chain_id.desc(),
        ('diff', ASCENDING): diff_sum.asc(),
        ('diff', DESCENDING): diff_sum.desc(),
        ('count', ASCENDING): chain_count.asc(),
        ('count', DESCENDING): chain_count.desc(),
        ('level', ASCENDING): max_level.asc().nullsfirst(),
        ('level', DESCENDING): max_level.desc().nullslast(),
        ('base', ASCENDING): base_pokemon.asc(),
        ('base', DESCENDING): base_pokemon.desc()
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

    pager = query.paginate(page_number, item_count)
    chain_details = {}
    for row in pager.items:
        chain_details[row.evolution_chain_id] = {
            'difficulty': row.difficulty,
            'chain_count': row.chain_count,
            'base_pokemon': row.base_pokemon,
            'max_level': row.max_level
            }

    return pager, chain_details


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
    pager, chain_details = _query_sorted_evolutions(
        sort_key, sort_order, page_number, item_count)
    valid_chains = list(chain_details.keys())
    selection_filter = Evolution.evolution_chain_id.in_(valid_chains)
    rows = db.session.query(Evolution).filter(selection_filter).all()

    data = defaultdict(dict)
    stages = defaultdict(list)
    for row in rows:
        r_id = row.evolution_chain_id
        stages[r_id].append(row.to_dict())

        if r_id not in data:
            # Copy over the chain details, once per chain.
            data[r_id]['id'] = r_id
            for k, v in chain_details[r_id].items():
                data[r_id][k] = v

    for key, value in stages.items():
        data[key]['stages'] = _sort_evolution_stages(value)

    s_key = {
        'chain': 'evolution_chain_id',
        'diff': 'difficulty',
        'count': 'chain_count',
        'base': 'base_pokemon',
        'level': 'max_level'
        }.get(sort_key, 'evolution_chain_id')

    def key(it):
        val = it[s_key] if s_key in it else it['id']
        default = 10000 if sort_key == DESCENDING else 0
        return default if val is None else val

    is_reverse = (sort_order == DESCENDING)
    data = sorted(data.values(), key=key, reverse=is_reverse)
    return _pager(pager, data)


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

    result = [row.to_dict(show=Evolution.EXTRA_FIELDS) for row in rows]
    sorted_result = _sort_evolution_stages(result)

    levels = [it['level'] for it in sorted_result if it['level'] is not None]
    base_id = sorted_result[0]['evolves_from']['id'] if sorted_result else None
    data = {
        'id': chain_id,
        'difficulty': sum([it['difficulty'] for it in sorted_result]),
        'base_pokemon': query_pokemon(base_id),
        'chain_count': len(sorted_result),
        'max_level': None if not levels else max(levels),
        'stages': sorted_result
        }

    return data


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
    is_descending = (sort_order == DESCENDING)
    default_sort = Type.id.desc() if is_descending else Type.id.asc()
    sort = {
        ('id', DESCENDING): Type.id.desc(),
        ('name', ASCENDING): Type.identifier.asc(),
        ('name', DESCENDING): Type.identifier.desc(),
        ('count', ASCENDING): Type.pokemon_count.asc(),
        ('count', DESCENDING): Type.pokemon_count.desc(),
        ('stats', ASCENDING): Type.stat_average.asc(),
        ('stats', DESCENDING): Type.stat_average.desc(),
        ('adv', ASCENDING): Type.relative_advantage.asc(),
        ('adv', DESCENDING): Type.relative_advantage.desc()
        }.get(sort_params, default_sort)

    query = Type.query.order_by(sort)
    pager = query.paginate(page_number, item_count)
    return _pager(pager)


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


def _query_related_pokemon(pokemon):
    """Searchs for the related evolutions of a list of Pokémon.

    Args:
        pokemon: A list of dictionary representations of models from the
            Pokémon database.

    Returns:
        A list of same-structured dicts containing the non-intersection Pokémon
        from the evolution chains specified by the input.
    """

    def get_evo(it): return it.evolution_chain_id
    evolution_chain_ids = list(filter(None, map(get_evo, pokemon)))
    poke_ids = set(map(lambda it: it.id, pokemon))
    evo_filter = Pokemon.evolution_chain_id.in_(evolution_chain_ids)
    id_filter = not_(Pokemon.id.in_(poke_ids))
    related_pokemon = Pokemon.query.filter(evo_filter, id_filter).all()
    return related_pokemon


def _search_pokemon(query, limit):
    """Searching for Pokémon based on an input query.

    Args:
        query: The text which should be searched for in the database.
        limit: The maximum number of results to receive from the search.

    Returns:
        A 3-tuple of (relevance, results, related_results). The relavance
        describes how relevant Pokémon are to the query in general. The related
        results include Pokémon which share evolution chains with of Pokémon in
        the primary search results.
    """
    similarities = [
        0.9 * func.similarity(Pokemon.identifier, query),
        1.1 * func.similarity(Pokemon.genus, query),
        0.1 * func.similarity(Pokemon.color, query)]

    similarity = sum(similarities)
    sorts = similarity.desc(), Pokemon.id.asc()

    check_identifier = similarity >= 0.2
    sql_query = Pokemon.query.add_columns(similarity).filter(check_identifier)
    result = sql_query.order_by(*sorts).limit(limit)
    if result.count() > 0:
        items, scores = zip(*result)
    else:
        items, scores = [], []

    related = _query_related_pokemon(items)
    relevance = max(scores, default=0)
    extra_cols = ['flavor_text', 'genus']
    return relevance, to_dict(items, extra_cols), to_dict(related, extra_cols)


def _search_types(query, limit):
    """Searches for types based on an input query.

    Args:
        query: The text which should be searched for in the database.
        limit: The maximum number of results to receive from the search.

    Returns:
        A 2-tuple of (relevance, results). The relavance describes how relevant
        types are to the query in general.
    """
    similarities = [
        func.similarity(Type.identifier, query),
        0.6 * func.similarity(Type.desc_info, query),
        0.2 * func.similarity(Type.desc_atk, query),
        0.2 * func.similarity(Type.desc_def, query),
        ]
    similarity = sum(similarities)

    check_identifier = similarity >= 0.3
    sql_query = Type.query.add_columns(similarity).filter(check_identifier)
    result = sql_query.order_by(similarity.desc()).limit(limit)
    if result.count() > 0:
        items, scores = zip(*result)
    else:
        items, scores = [], []

    relevance = max(scores, default=0)
    return relevance, to_dict(items, ['desc_info'])


def _search_result(score, data, related=None):
    """Standardizes the format of search result sections.

    Args:
        score: The relavance score for the entire section.
        data: The list of results returned by the search.
        related (optional): A list of results that are related to the results
            in data, but that would not be picked up by the query.

    Returns:
        A dict with 'relevance', 'data', and 'related' keys which map to the
        values given by the input arguments.
    """
    return {'relevance': score, 'data': data, 'related': related}


def search(query, limit=None, models=None):
    """Searches the database for Pokémon and type information.

    Args:
        query: The text used to search the database.
        limit: The maximum number of results for Pokémon and/or types.
        models: A string containing 'pokemon' and/or 'type', joined by a comma.

    Returns:
        The search results as a dict, with 'pokemon' and 'types' as keys. Each
        key maps to a dict created by the `search_result` function.
    """
    limit = limit or SEARCH_LIMIT
    models = models or ALL_MODELS

    out_types = set(map(str.strip, models.lower().split(',')))
    out = {}
    if 'pokemon' in out_types:
        pokemon_result = _search_pokemon(query, limit)
        out.update(pokemon=_search_result(*pokemon_result))
    else:
        out.update(pokemon=_search_result(0, []))

    if 'type' in out_types:
        type_result = _search_types(query, limit)
        out.update(types=_search_result(*type_result))
    else:
        out.update(types=_search_result(0, []))

    return out
