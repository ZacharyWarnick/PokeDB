
from flask import Blueprint, request, jsonify as flask_jsonify
from sqlalchemy import func, or_
from models import db, Pokemon, Evolution, Type
from pprint import pprint

api = Blueprint('api', 'api', url_prefix='/api')

ITEMS_PER_PAGE = 16
ASCENDING = 'ASC'
DESCENDING = 'DESC'


def parse_sort_args(req):
    sort_key = req.args.get('sort', '')
    sort_order = req.args.get('order', ASCENDING)
    page_number = 1
    try:
        page_number = int(req.args.get('page', 1))
    except ValueError:
        print('Page number could not be cast to int.')

    return sort_key, sort_order, page_number


def jsonify(obj, show=None):
    if isinstance(obj, dict):
        return flask_jsonify(obj)

    if isinstance(obj, list):
        if obj and isinstance(obj[0], dict):
            return flask_jsonify(obj)

        return flask_jsonify([it.to_dict(show=show) for it in obj])

    return flask_jsonify(obj.to_dict(show=show))


@api.route('/pokemon', methods=['GET'])
def get_pokemon_listing():
    sort_key, sort_order, page_number = parse_sort_args(request)

    sort_params = (sort_key, sort_order)
    default_sort = Pokemon.id.asc()
    sort = {
        ('id', DESCENDING): Pokemon.id.desc(),
        ('name', ASCENDING): Pokemon.name.asc(),
        ('name', DESCENDING): Pokemon.name.desc()
        }.get(sort_params, default_sort)

    query = Pokemon.query.order_by(sort)
    items = query.paginate(page_number, ITEMS_PER_PAGE).items

    return jsonify([it.to_dict() for it in items])


@api.route('/pokemon/<int:pokemon>', methods=['GET'])
@api.route('/pokemon/<string:pokemon>', methods=['GET'])
def get_pokemon(pokemon):
    filter_key = 'identifier' if isinstance(pokemon, str) else 'id'
    filter_args = {filter_key: pokemon}

    query = Pokemon.query.filter_by(**filter_args)
    item = query.first_or_404()

    return jsonify(item.to_dict(show=Pokemon.EXTRA_FIELDS))


@api.route('/evolutions', methods=['GET'])
def get_evolutions():
    sort_key, sort_order, page_number = parse_sort_args(request)

    sort_params = (sort_key, sort_order)
    default_sort = Evolution.evolution_chain_id.asc()

    chain_count = func.count(func.distinct(Evolution.id)).label('chain_count')
    diff_avg = func.avg(Evolution.difficulty).label('difficulty')
    max_level = func.max(Evolution.level).label('max_level')
    base_pokemon = func.min(
        Evolution.evolves_from_pokemon_id).label('base_pokemon')

    sort = {
        ('chain', DESCENDING): Evolution.evolution_chain_id.desc(),
        ('diff', ASCENDING): diff_avg.asc(),
        ('diff', DESCENDING): diff_avg.desc(),
        ('count', ASCENDING): chain_count.asc(),
        ('count', DESCENDING): chain_count.desc(),
        ('level', ASCENDING): chain_count.asc(),
        ('level', DESCENDING): chain_count.desc(),
        ('base', ASCENDING): base_pokemon.asc(),
        ('base', DESCENDING): base_pokemon.desc()
        }.get(sort_params, default_sort)

    # Get ordered chains of evolutions.
    join_rel = or_(
        Pokemon.id == Evolution.evolves_from_pokemon_id,
        Pokemon.id == Evolution.pokemon_id)

    entities = [
        Evolution.evolution_chain_id, base_pokemon, chain_count, diff_avg,
        max_level]

    query = db.session.query(Evolution).with_entities(*entities)
    query = query.join(Pokemon, join_rel)
    query = query.group_by(Evolution.evolution_chain_id)
    query = query.order_by(sort)

    result = query.paginate(page_number, ITEMS_PER_PAGE).items
    chain_details = {}
    for row in result:
        chain_details[row.evolution_chain_id] = {
            'difficulty': row.difficulty,
            'chain_count': row.chain_count,
            'base_pokemon': row.base_pokemon,
            'max_level': row.max_level
            }

    valid_chains = list(chain_details.keys())
    selection_filter = Evolution.evolution_chain_id.in_(valid_chains)
    query = db.session.query(Evolution).filter(selection_filter)
    rows = query.all()

    data = {}
    for row in rows:
        r_id = row.evolution_chain_id
        chain_info = data.get(r_id, {})
        if not chain_info:
            chain_info['id'] = r_id
            for k, v in chain_details[r_id].items():
                chain_info[k] = v

            data[r_id] = chain_info

        stage_key = str(row.pokemon_id)
        chain_stages = chain_info.get(stage_key, [])
        chain_stages.append(row.to_dict())

        data[r_id][stage_key] = chain_stages

    def key(it): return it[sort_key] if sort_key in it else it['id']

    is_reverse = sort_order != ASCENDING
    output = list(data.values())
    output.sort(key=key, reverse=is_reverse)

    pprint(output)
    return jsonify(output)


@api.route('/evolutions/<int:chain>', methods=['GET'])
def get_evolution(chain):
    query = Evolution.query.filter_by(evolution_chain_id=chain)
    items = query.all()

    return jsonify([it.to_dict() for it in items])


@api.route('/types', methods=['GET'])
def get_types():
    sort_key, sort_order, page_number = parse_sort_args(request)

    sort_params = (sort_key, sort_order)
    default_sort = Type.id.asc()
    sort = {
        ('id', DESCENDING): Type.id.desc(),
        ('name', ASCENDING): Type.name.asc(),
        ('name', DESCENDING): Type.name.desc(),
        ('pokemon_count', ASCENDING): Type.pokemon_count.asc(),
        ('pokemon_count', DESCENDING): Type.pokemon_count.desc(),
        ('stat_average', ASCENDING): Type.stat_average.asc(),
        ('stat_average', DESCENDING): Type.stat_average.desc(),
        ('relative_advantage', ASCENDING): Type.relative_advantage.asc(),
        ('relative_advantage', DESCENDING): Type.relative_advantage.desc()
        }.get(sort_params, default_sort)

    query = Type.query.order_by(sort)
    items = query.paginate(page_number, ITEMS_PER_PAGE).items

    return jsonify(items)


@api.route('/types/<int:a_type>', methods=['GET'])
@api.route('/types/<string:a_type>', methods=['GET'])
def get_type(a_type):
    filter_key = 'identifier' if isinstance(a_type, str) else 'id'
    filter_args = {filter_key: a_type}

    query = Type.query.filter_by(**filter_args)
    item = query.first_or_404()

    return jsonify(item.to_dict(show=Type.EXTRA_FIELDS))
