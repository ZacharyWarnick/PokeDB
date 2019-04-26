"""Exposes a Flask Blueprint which provides an API for accessing the database.

General Query Parameters:
    sort: Unique to each listing type, but always a string value.
    order: The sort order. Either 'ASC' (ascending) or 'DESC' (descending).
    page: The index for pagination. This should always be an integer value.

Parameter names are case sensitive, but parameter values (except 'page') are
case tolerant. By default, every page returns 16 items.

Example Requests:
- /api/pokemon?sort=name&order=ASC&page=2
- /api/pokemon/1
- /api/pokemon/bulbasaur
- /api/evolutions?sort=base&order=DESC
- /api/evolutions/1
- /api/types?sort=name&order=ASC&page=2
- /api/types/1
- /api/types/normal

Items page endpoints ARE case sensitive. The following requests would fail:
- /api/pokemon/Bulbasaur
- /api/types/Grass

To see information about the queries, refer to the `data` module.
"""
import data

from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix='/api')


def parse_sort_args(req):
    """Parses listing page query parameters.

    If a query parameter is not given, then a default is supplied.

    Query Parameters:
        sort: The sort key to use.
        order: Either 'ASC' or 'DESC', see data.ASCENDING and data.DESCENDING.
        page: The page index for pagination (>= 1).

    Arguments:
        req: The active `flask.request` object.

    Returns:
        A 3-tuple containing (sort_key, sort_order, page_index).
    """
    sort_key = req.args.get('sort', '').lower()
    sort_order = req.args.get('order', data.ASCENDING).upper()
    try:
        page_number = int(req.args.get('page', 1))
    except ValueError:
        # Just send user to the first page on a bad query parameter.
        page_number = 1

    return sort_key, sort_order, page_number


@api.route('/pokemon', methods=['GET'])
def get_pokemon_listing():
    sort_key, sort_order, page_number = parse_sort_args(request)
    listing = data.query_pokemon_list(sort_key, sort_order, page_number)
    return jsonify(listing)


@api.route('/pokemon/<int:pokemon>', methods=['GET'])
@api.route('/pokemon/<string:pokemon>', methods=['GET'])
def get_pokemon(pokemon):
    return jsonify(data.query_pokemon(pokemon))


@api.route('/evolutions', methods=['GET'])
def get_evolutions():
    sort_key, sort_order, page_number = parse_sort_args(request)
    listing = data.query_evolution_list(sort_key, sort_order, page_number)
    return jsonify(listing)


@api.route('/evolutions/<int:chain>', methods=['GET'])
def get_evolution(chain):
    return jsonify(data.query_evolution(chain))


@api.route('/types', methods=['GET'])
def get_types():
    sort_key, sort_order, page_number = parse_sort_args(request)
    items = data.query_type_list(sort_key, sort_order, page_number)
    return jsonify(items)


@api.route('/types/<int:a_type>', methods=['GET'])
@api.route('/types/<string:a_type>', methods=['GET'])
def get_type(a_type):
    return jsonify(data.query_type(a_type))


@api.route('/types/<int:a_type>/related', methods=['GET'])
def get_related_pokemon(a_type):
    return jsonify(data.query_pokemon_for_type(a_type))


@api.route('/tests', methods=['GET'])
def get_test_results():  # pragma: no cover
    from tests import api_util as util
    result = util.get_coverage_result()
    del util
    return result


@api.route('/search', methods=['GET'])
def search():
    q = request.args.get('q', '')
    limit = request.args.get('limit')
    models = request.args.get('models')
    return jsonify(data.search(q, limit, models))
