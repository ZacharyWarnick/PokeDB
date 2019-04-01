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
        'from': None,
        'to': ['gyarados'],
        'min_level': 20,
        'gender': None,
        'hold_item': None,
    },
    'gyarados': {
        'from': ['magikarp'],
        'to': None,
        'min_level': None,
        'gender': None,
        'hold_item': None,
    },
    'ekans': {
        'from': None,
        'to': ['arbok'],
        'min_level': 22,
        'gender': None,
        'hold_item': None,
    },
    'arbok': {
        'from': ['ekans'],
        'to': None,
        'min_level': None,
        'gender': None,
        'hold_item': None,
    },
    'sandshrew': {
        'from': None,
        'to': ['sandslash'],
        'min_level': 22,
        'gender': None,
        'hold_item': None,
    },
    'sandslash': {
        'from': ['sandshrew'],
        'to': None,
        'min_level': None,
        'gender': None,
        'hold_item': None,
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

EVOLUTION_CHAINS = {
    'ekans': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'arbok': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'sandshrew': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'sandslash': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'magikarp': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'gyarados': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    }
}

EVOLUTION_STEPS = {
    'ekans': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'arbok': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'sandshrew': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'sandslash': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'magikarp': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    },
    'gyarados': {
        'evolves_from': '', #?
        'trigger_item': '', #?
        'location': '', #?
    }
}

LOCATIONS = {
    'ekans': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'arbok': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'sandshrew': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'sandslash': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'magikarp': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    },
    'gyarados': {
        'identifier': '', #?
        'name': '', #?
        'subtitle': '', #?
    }
}

FORMS = {
    'ekans': {
        'form_label': '', #?
        'identifier': '', #?
        'pokemon_id': 23,
        'pokemon_name': 'Ekans'
    },
    'arbok': {
        'form_label': '', #?
        'identifier': '', #?
        'pokemon_id': 24,
        'pokemon_name': 'Arbok'
    },
    'sandshrew': {
        'form_label': '', #?
        'identifier': '', #?
        'pokemon_id': 27,
        'pokemon_name': 'Sandshrew'
    },
    'sandslash': {
        'form_label': '', #?
        'identifier': '', #?
        'pokemon_id': 28,
        'pokemon_name': 'Sandslash'
    },
    'magikarp': {
        'form_label': '', #?
        'identifier': '', #?
        'pokemon_id': 129,
        'pokemon_name': 'Magikarp'
    },
    'gyarados': {
        'form_label': '', #?
        'identifier': '', #?
        'pokemon_id': 130,
        'pokemon_name': 'Gyarados'
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