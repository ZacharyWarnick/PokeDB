# from ??????????? import Pokemon, Evolutions, Types, Forms, BaseStats
from flask import Blueprint, request, jsonify, session
from sqlalchemy import create_engine

# So I pretty much made two options because I wasn't sure
# The first one starts here and there will be a comment break
# for the next option

database = create_engine('sqlite:???????????')
app = Flask(__name__)


class Pokemon:
    def get(self):
        conn = database.connect()  # Connect to database
        # Performs query and returns json result
        query = conn.execute("select * from Pokemon")
        # Fetches first column that is Employee ID
        return {'Pokemon': [i[0] for i in query.cursor.fetchall()]}


class Evolutions:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Evolutions")
        return {'Evolutions': [i[0] for i in query.cursor.fetchall()]}


class Types:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Types")
        return {'Types': [i[0] for i in query.cursor.fetchall()]}


class Forms:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Forms")
        return {'Forms': [i[0] for i in query.cursor.fetchall()]}


class BaseStats:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Base_Stats")
        return {'Base_Stats': [i[0] for i in query.cursor.fetchall()]}


# Everything before this was something I found online and wasn't sure
# Everything after is another option that follows the original link
# Jake sent in back-end. It has areas that need to be filled in with ???

api = Blueprint('api', 'api', url_prefix='/api')


@api.route('/????????????', methods=['GET'])
def api_pokemon():
    pokemon = request.get_json()
    pokemons = ???????????????.query.filter_by(status=1).join(Pokemon).order_by(??????????.id.desc()).all()
    all_pokemons = {'Pokemon': [pokemon.to_json() for pokemon in pokemons]}

    return jsonify(all_pokemon)


@api.route('/????????????', methods=['GET'])
def api_evolutions():
    evolution = request.get_json()
    evolutions = ???????????????.query.filter_by(status=1).join(Evolution).order_by(??????????.id.desc()).all()
    all_evolutions = {'Pokemon': [evolution.to_json()
                                  for evolution in evolutions]}

    return jsonify(all_evolutions)


@api.route('/????????????', methods=['GET'])
def api_types():
    type = request.get_json()
    types = ???????????????.query.filter_by(status=1).join(Types).order_by(??????????.id.desc()).all()
    all_types = {'Type': [type.to_json() for type in types]}

    return jsonify(all_types)


@api.route('/????????????', methods=['GET'])
def api_forms():
    form = request.get_json()
    forms = ???????????????.query.filter_by(status=1).join(Forms).order_by(??????????.id.desc()).all()
    all_forms = {'Form': [form.to_json() for form in forms]}

    return jsonify(all_forms)


@api.route('/????????????', methods=['GET'])
def api_base_stats():
    base_stat = request.get_json()
    base_stats = ???????????????.query.filter_by(status=1).join(BaseStats).order_by(??????????.id.desc()).all()
    all_base_stats = {'Form': [form.to_json() for form in forms]}

    return jsonify(all_base_stats)

# if __name__ == '__main__':
#      app.run()
