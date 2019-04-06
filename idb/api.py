
import ast

from flask import Blueprint, request, jsonify
from models import Pokemon, Evolution, Type

api = Blueprint('api', 'api', url_prefix='/api')

ITEMS_PER_PAGE = 16
ASCENDING = 'ASC'
DESCENDING = 'DESC'


def parse_sort_args(req):
    sort_key = req.args.get('sort', None)
    sort_order = req.args.get('order', ASCENDING)
    page_number = req.args.get('page', 1)
    return sort_key, sort_order, page_number


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
    default_sort = Evolution.id.asc()
    sort = {
        ('id', DESCENDING): Evolution.id.desc(),
        ('name', ASCENDING): Evolution.name.asc(),
        ('name', DESCENDING): Evolution.name.desc()
        }.get(sort_params, default_sort)

    query = Evolution.query.order_by(sort)
    items = query.paginate(page_number, ITEMS_PER_PAGE).items

    return jsonify(items)


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
