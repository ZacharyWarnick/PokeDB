#from some_folder import Pokemon, Evolutions, Types, Forms, BaseStats
from flask import Blueprint, request, jsonify, session

api = Blueprint('api', 'api', url_prefix='/api')

@api.route('/wherever', methods=['GET'])

# Retrieves/adds polls from/to the database
def api_pokemon():

    pokemon = [pokemon.to_json() for pokemon in Pokemon.query.all()]

    return jsonify(pokemon)

def api_evolutions():
    
    evolutions = [evolutions.to_json() for evolutions in Evolutions.query.all()]

    return jsonify(evolutions)

def api_types():
    
    types = [types.to_json() for types in Types.query.all()]

    return jsonify(types)

def api_forms():
    
    forms = [forms.to_json() for forms in Forms.query.all()]

    return jsonify(forms)

def api_base_stats():
    
    base_stats = [base_stats.to_json() for base_stats in BaseStats.query.all()]

    return jsonify(base_stats)
