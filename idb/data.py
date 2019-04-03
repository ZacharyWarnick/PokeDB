POKEMON = {
    'ekans': {
        'id': 23,
        'description': 'Snake that is 3 meters long and weighs around 6.9 kilograms.',
        'category': 'Snake',
        'type': ['poison'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png'

    },
    'arbok': {
        'id': 24,
        'description': 'Cobra that is 3.5 meters long and weighs around 65 kilograms.',
        'category': 'Cobra',
        'type': ['poison'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png'
    },
    'sandshrew': {
        'id': 27,
        'description': 'Mouse that is 0.6 meters tall and weighs around 12 kilograms.',
        'category': 'Mouse',
        'type': ['ground'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png'
    },
    'sandslash': {
        'id': 28,
        'description': 'Mouse that is 1 meters tall and weighs around 29.5 kilograms.',
        'category': 'Mouse',
        'type': ['ground'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png'
    },
    'magikarp': {
        'id': 129,
        'description': 'Fish that is 0.9 meters long and weighs around 10.0 kilograms.',
        'category': 'Fish',
        'type': ['water'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png'
    },
    'gyarados': {
        'id': 130,
        'description': 'Atrocious Pokémon that is 3.5 meters long and weighs around 65 kilograms.',
        'category': 'Atrocious Pokémon',
        'type': ['water', 'flying'],
        'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png'
    }
}

EVOLUTION = {
    'magikarp': {
        "evolves_from": 129,
        "chain": 64,
        "trigger": "level-up",
        "level": 20,
        "id": 75
    },
    'gyarados': {
        "evolves_from": 252,
        "chain": 130,
        "trigger": "level-up",
        "level": 16,
        "id": 130
    },
    'ekans': {
        "evolves_from": 173,
        "chain": 14,
        "trigger": "level-up",
        "happiness": 220,
        "id": 23
    },
    'arbok': {
        "evolves_from": 35,
        "chain": 14,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 24
    },
    'sandshrew': {
        "evolves_from": 39,
        "chain": 16,
        "trigger": "use-item",
        "trigger_item": "moon-stone",
        "id": 27
    },
    'sandslash': {
        "evolves_from": 41,
        "chain": 17,
        "trigger": "level-up",
        "level": 22,
        "id": 28
    }
}

TYPE = {
    'water': {
        'advantages': ['ground', 'rock', 'fire'],
        'weaknesses': ['grass', 'electric'],
        'pokemon': ['magikarp', 'gyarados']
    },
    'flying': {
        'advantages': ['fighting', 'bug', 'grass'],
        'weaknesses': ['rock', 'electric', 'ice'],
        'pokemon': ['gyarados']
    },
    'ground': {
        'advantages': ['poison', 'rock', 'fire', 'steel', 'electric'],
        'weaknesses': ['water', 'grass', 'ice'],
        'pokemon': ['sandslash', 'sandshrew']
    },
    'poison': {
        'advantages': ['grass', 'fairy'],
        'weaknesses': ['ground', 'psychic'],
        'pokemon': ['ekans', 'arbok']
    },
}

FORMS = {
    'sandshrew': {
        "pokemon_name": "Alolan Sandshrew",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 27,
        "id": 10203
    },
    'sandslash': {
        "pokemon_name": "Alolan Sandslash",
        "form_label": "Alola Form",
        "identifier": "alola",
        "pokemon_id": 28,
        "id": 10204
    },
    'gyarados': {
        "pokemon_name": "Mega Gyarados",
        "form_label": "Mega Gyarados",
        "identifier": "mega",
        "pokemon_id": 130,
        "id": 10141
    }
}

BASE_STATS = {
    'ekans': {
        'hp': 35,
        'atk': 60,
        'def': 44,
        'sp_atk': 40,
        'sp_def': 54,
        'spd': 55
    },
    'arbok': {
        'hp': 60,
        'atk': 95,
        'def': 69,
        'sp_atk': 65,
        'sp_def': 79,
        'spd': 80
    },
    'sandshrew': {
        'hp': 50,
        'atk': 75,
        'def': 85,
        'sp_atk': 20,
        'sp_def': 30,
        'spd': 40
    },
    'sandslash': {
        'hp': 75,
        'atk': 100,
        'def': 110,
        'sp_atk': 45,
        'sp_def': 55,
        'spd': 65
    },
    'magikarp': {
        'hp': 20,
        'atk': 10,
        'def': 55,
        'sp_atk': 15,
        'sp_def': 20,
        'spd': 80
    },
    'gyarados': {
        'hp': 95,
        'atk': 125,
        'def': 79,
        'sp_atk': 60,
        'sp_def': 100,
        'spd': 81
    }
}
