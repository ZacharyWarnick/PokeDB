POKEMON = {
    'ekans': {
        'id': 23,
        'description': 'Snake that is 3 meters long and weighs around 6.9 kilograms.',
        'category': 'Snake',
        'type': ['poison']
    },
    'arbok': {
        'id': 24,
        'description': 'Cobra that is 3.5 meters long and weighs around 65 kilograms.',
        'category': 'Cobra',
        'type': ['poison']
    },
    'sandshrew': {
        'id': 27,
        'description': 'Mouse that is 0.6 meters tall and weighs around 12 kilograms.',
        'category': 'Mouse',
        'type': ['ground']
    },
    'sandslash': {
        'id': 28,
        'description': 'Mouse that is 1 meters tall and weighs around 29.5 kilograms.',
        'category': 'Mouse',
        'type': ['ground']
    },
    'magikarp': {
        'id': 129,
        'description': 'Fish that is 0.9 meters long and weighs around 10.0 kilograms.',
        'category': 'Fish',
        'type': ['water']
    },
    'gyarados': {
        'id': 130,
        'description': 'Atrocious Pokémon that is 3.5 meters long and weighs around 65 kilograms.',
        'category': 'Atrocious Pokémon',
        'type': ['water', 'flying']
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
