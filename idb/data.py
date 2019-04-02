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

var evolution_info = {
    'ekans' : {
        'species' : 'ekans',
        'first' : {
            'name' : 'Ekans',
            'id' : 23,
            'types': '[this.$types['poison']]'
        },
        'second' : {
        'name' : 'Arbok',
        'id' : 24,
        'types': '[this.$types['poison']]'
        }
    },
    'sandshrew' : {
        'species' : 'sandshrew',
        'first' : {
            'name' : 'Sandshrew',
            'id' : 27,
            'types' : '[this.$types['ground']]'
        },
        'second' : {
        'name' : 'Sandslash',
        'id' : 28,
        'types': '[this.$types['ground']]'
        }
    },
    'magikarp' : {
        'species': 'magikarp',
        'first': {
            'name': 'Magikarp',
            'id': 129,
            'types': '[this.$types['water']]'
        },
        'second' : {
        'name' : 'Gyarados',
        'id' : 130,
        'types': '[this.$types['water'], this.$types['flying']]'
        }
    }
}

ALL = {
    'ekans': {
        'display_name' : ['Ekans'],
        'id' : 23,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/thumb/f/fa/023Ekans.png/250px-023Ekans.png'],
        'types' : '[this.$types['poison']]',
        'flavor_text' :
            ['Ekans curls itself up in a spiral while it rests. Assuming this position allows it to quickly respond to a threat from any direction with a glare from its upraised head.'],
        'stats' : {
            BASE_STATS['ekans']
            # 'hp' : 35,
            # 'atk' : 60,
            # 'def' : 44,
            # 'sp_atk' : 40,
            # 'sp_def' : 54,
            # 'spd' : 55
        },
        'ev' : evolution_info['ekans']
    },
    'arbok' : {
        'display_name' : ['Arbok'],
        'id' : 24,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/thumb/c/cd/024Arbok.png/250px-024Arbok.png'],
        'types' : '[this.$types['poison']]',
        'flavor_text' :
            ['The latest research has determined that there are over 20 possible arrangements of the patterns on its stomach.'],
        'stats' : {
            BASE_STATS['arbok']
            # 'hp' : 60,
            # 'atk' : 95,
            # 'def' : 69,
            # 'sp_atk' : 65,
            # 'sp_def' : 79,
            # 'spd' : 80
        },
        'ev' : evolution_info['ekans']
    },
    'sandshrew' : {
        'display_name' : ['Sandshrew'],
        'id' : 27,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/9/9e/027Sandshrew.png'],
        'types' : '[this.$types['ground']]',
        'flavor_text' :
            ['Sandshrew has a very dry hide that is extremely tough. The Pokémon can roll into a ball that repels any attack. At night, it burrows into the desert sand to sleep.'],
        'stats' : {
            BASE_STATS['sandshrew']
            # 'hp' : 50,
            # 'atk' : 75,
            # 'def' : 85,
            # 'sp_atk' : 20,
            # 'sp_def' : 30,
            # 'spd' : 40
        },
        'ev' : evolution_info['sandshrew']
    },
    'sandslash' : {
        'display_name' : ['Sandslash'],
        'id' : 28,
        'sprite' :
            ['https://assets.pokemon.com/assets/cms2/img/pokedex/full/028.png'],
        'types': '[this.$types['ground']]',
        'flavor_text' :
            ['Sandslash can roll up its body as if it were a ball covered with large spikes. In battle, this Pokémon will try to make the foe flinch by jabbing it with its spines. It then leaps at the stunned foe to tear wildly with its sharp claws.'],
        'stats' : {
            BASE_STATS['sandslash']
            # 'hp' : 75,
            # 'atk' : 100,
            # 'def' : 110,
            # 'sp_atk' : 45,
            # 'sp_def' : 55,
            # 'spd' : 65
        },
        'ev' : evolution_info['sandshrew']
    },
    'magikarp' : {
        'display_name' : ['Magikarp'],
        'id' : 129,
        'sprite' :
            ['https://cdn.bulbagarden.net/upload/thumb/0/02/129Magikarp.png/250px-129Magikarp.png'],
        'types': '[this.$types['water']]',
        'flavor_text' :
            ['Magikarp is virtually useless in battle as it can only splash around. As a result, it is considered to be weak. However, it is actually a very hardy Pokémon that can survive in any body of water no matter how polluted it is.'],
        'stats' : {
            BASE_STATS['magikarp']
            # 'hp' : 20,
            # 'atk' : 10,
            # 'def' : 55,
            # 'sp_atk' : 15,
            # 'sp_def' : 20,
            # 'spd' : 80
        },
        'ev' : evolution_info['magikarp']
    },
    'gyarados' : {
        'display_name' : ['Gyarados'],
        'id' : 130,
        'sprite' :
            ['https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png'],
        'types' : '[this.$types['water'], this.$types['flying']]',
        'flavor_text' :
            ['Once Gyarados goes on a rampage, its ferociously violent blood doesn’t calm until it has burned everything down. There are records of this Pokémon’s rampages lasting a whole month.'],
        'stats' : {
            BASE_STATS['gyarados']
            # 'hp' : 95,
            # 'atk' : 125,
            # 'def' : 79,
            # 'sp_atk' : 60,
            # 'sp_def' : 100,
            # 'spd' : 81
        },
        'ev' : evolution_info['magikarp']
    }
}

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
        'to': ALL['gyarados']['id'],
        'min_level': 20,
        'gender': None,
        'hold_item': None,
    },
    'gyarados': {
        'from': ALL['magikarp']['id'],
        'to': None,
        'min_level': None,
        'gender': None,
        'hold_item': None,
    },
    'ekans': {
        'from': None,
        'to': ALL['arbok']['id'],
        'min_level': 22,
        'gender': None,
        'hold_item': None,
    },
    'arbok': {
        'from': ALL['ekans']['id'],
        'to': None,
        'min_level': None,
        'gender': None,
        'hold_item': None,
    },
    'sandshrew': {
        'from': None,
        'to': ALL['sandslash']['id'],
        'min_level': 22,
        'gender': None,
        'hold_item': None,
    },
    'sandslash': {
        'from': ALL['sandshrew']['id'],
        'to': None,
        'min_level': None,
        'gender': None,
        'hold_item': None,
    }
}

TYPE = {
    'water': {
        'info' : 'Water is one of the three basic elemental types along with Fire and Grass,'\
                'which constitute the three starter Pokémon. This creates a simple triangle'\
                'to explain the type concept easily to new players. Water is the most common'\
                'type with over 100 Pokémon, which are based on a wide variety of fish and'\
                'other sea-dwelling creatures.',
        'info2' : 'Notable Trainers who specialize in Water-type Pokémon include Misty of Cerulean City,'\
                  'Juan and Wallace of Sootopolis City, Crasher Wake of Pastoria City, Cress of Striaton City,'\
                  'Marlon of Humilau City, Siebold of the Kalos Elite Four, and Trial Captain Lana of Konikoni City.'\
                  'Prior to changes in Generation IV, all damaging Water-type moves were special,'\
                  'but they may now also be physical depending on the attack.',
        'image' : 'https://pokeweakness.com/images/1891870-131lapras.png',
        'advantages': ['ground', 'rock', 'fire'],
        'weaknesses': ['grass', 'electric'],
        'pokemon': [ALL['magikarp']['id'], ALL['gyarados']['id']]
        "damage_class" : 'special',
        'identifier' : 'water',
        'vs_normal' : 1.0,
        'vs_fighting' : 1.0,
        'vs_flying' : 1.0,
        'vs_poison' : 1.0,
        'vs_ground' : 2.0,
        'vs_rock' :  2.0,
        'vs_bug' : 1.0,
        'vs_ghost' : 1.0,
        'vs_steel' : 1.0,
        'vs_fire' : 2.0,
        'vs_water' : 0.5,
        'vs_grass' : 0.5,
        'vs_electric' : 1.0,
        'vs_psychic' : 1.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 0.5,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 11
    },
    'flying': {
        'info' : 'Most Flying type Pokémon are based on birds or insects, along with some mythical creatures like dragons.'\
        'On average they are faster than any other type. Nearly every Flying type has Flying as the secondary type,'\
        'usually with Normal.'\
        'There is only one pure Flying Pokémon (Tornadus), and one line with Flying as a primary type (Noibat/Noivern).',
        'info2' : 'Notable Trainers who specialize in Flying-type Pokémon are the Gym Leaders Falkner of Violet City,'\
        'Winona of Fortree City, Skyla of Mistralton City, and Kahili of Alola Elite Four.'\
        'Prior to changes in Generation IV, all damaging Flying-type moves were physical,'\
        'but they may now also be special depending on the attack.',
        'image' : 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/018.png',
        'advantages': ['fighting', 'bug', 'grass'],
        'weaknesses': ['rock', 'electric', 'ice'],
        'pokemon': [ALL['gyarados']['id']]
        'damage_class' : 'physical',
        'identifier' : 'flying',
        'vs_normal' : 1.0,
        'vs_fighting' : 2.0,
        'vs_flying' : 1.0,
        'vs_poison' : 1.0,
        'vs_ground' : 1.0,
        'vs_rock' : 0.5,
        'vs_bug' : 2.0,
        'vs_ghost' : 1.0,
        'vs_steel' : 0.5,
        'vs_fire' : 1.0,
        'vs_water' : 1.0,
        'vs_grass' : 2.0,
        'vs_electric' : 0.5,
        'vs_psychic' : 1.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 3
    },
    'ground': {
        'info' : 'Ground is one of the strongest types offensively:'\
        'it is super-effective against five other types (as is Fighting)'\
        'and Earthquake is one of the strongest moves in the game with power and accuracy both 100.'\
        'Unfortunately, many Ground type Pokémon are dual Rock types, lumbering them with 4x Grass and Water disadvantages.',
        'info2' : 'Notable Trainers who specialize in Ground-type Pokémon are Giovanni of Viridian City,'\
        'Bertha of the Sinnoh Elite Four, Clay of Driftveil City, and Island Kahuna Hapu of Poni Island.'\
        'Prior to changes in Generation IV, all damaging Ground-type moves were physical,'\
        'but they may now also be special depending on the attack.',
        'image' : 'https://cdn.bulbagarden.net/upload/3/31/050Diglett.png',
        'advantages': ['poison', 'rock', 'fire', 'steel', 'electric'],
        'weaknesses': ['water', 'grass', 'ice'],
        'pokemon': [ALL['sandslash']['id'], ALL['sandshrew']['id']]
        'damage_class' : 'physical',
        'identifier': 'ground',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 0.0,
        'vs_poison': 2.0,
        'vs_ground': 1.0,
        'vs_rock': 2.0,
        'vs_bug': 0.5,
        'vs_ghost': 1.0,
        'vs_steel': 2.0,
        'vs_fire': 2.0,
        'vs_water': 1.0,
        'vs_grass': 0.5,
        'vs_electric': 2.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 5
    },
    'poison': {
        'info' : 'The Poison type is regarded as one of the weakest offensively.'\
        'Prior to Pokémon X/Y it was super-effective only against Grass'\
        '(many of which are dual Poison so neutralizes the effect).'\
        'It now has an extra advantage against the new Fairy type.'\
        'In the first generation it was also super-effective against Bug but this was changed.'\
        'It fares a little better defensively but its best advantage is through status moves like Toxic.',
        'info2' : 'Notable Trainers who specialize in Poison-type Pokémon include Janine of Fuchsia City,'\
        'her father Koga of the Indigo Plateau Elite Four, Roxie of Virbank City, and Team Skull Admin Plumeria.'\
        'Some villainous teams, such as Team Rocket, also frequently use Poison-type Pokémon.'\
        'Prior to changes in Generation IV, all damaging Poison-type moves were physical,'\
        'but they may now also be special depending on the attack.',
        'image' : 'http://bogleech.com/pokemon/koffing.png',
        'advantages': ['grass', 'fairy'],
        'weaknesses': ['ground', 'psychic'],
        'pokemon': [ALL['ekans']['id'], ALL['arbok']['id']]
        'damage_class': 'physical',
        'identifier': 'poison',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 0.5,
        'vs_ground': 0.5,
        'vs_rock': 0.5,
        'vs_bug': 1.0,
        'vs_ghost': 0.5,
        'vs_steel': 0.0,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 2.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 2.0,
        'id': 4
    },
    'normal' : {
        'info' : '',
        'info2' : '',
        'image' : '',
        'advantages' : '',
        'weaknesses' : '',
        'pokemon' : '',
        'damage_class': 'physical',
        'identifier': 'normal',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 0.5,
        'vs_bug': 1.0,
        'vs_ghost': 0.0,
        'vs_steel': 0.5,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 1


    },
    'fighting': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': '',
        'identifier': '',
        'damage_class': 'physical',
        'identifier': 'fighting',
        'vs_normal': 2.0,
        'vs_fighting': 1.0,
        'vs_flying': 0.5,
        'vs_poison': 0.5,
        'vs_ground': 1.0,
        'vs_rock': 2.0,
        'vs_bug': 0.5,
        'vs_ghost': 0.0,
        'vs_steel': 2.0,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 0.5,
        'vs_ice': 2.0,
        'vs_dragon': 1.0,
        'vs_dark': 2.0,
        'vs_fairy': 0.5,
        'id': 2
    },
    'rock': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'physical',
        'identifier' : 'rock',
        'vs_normal' : 1.0,
        'vs_fighting' : 0.5,
        'vs_flying' : 2.0,
        'vs_poison' : 1.0,
        'vs_ground' : 0.5,
        'vs_rock' : 1.0,
        'vs_bug' : 2.0,
        'vs_ghost' : 1.0,
        'vs_steel' : 0.5,
        'vs_fire' : 2.0,
        'vs_water' : 1.0,
        'vs_grass' : 1.0,
        'vs_electric' : 1.0,
        'vs_psychic' : 1.0,
        'vs_ice' : 2.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 6

    },
    'bug': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'physical',
        'identifier' : 'bug',
        'vs_normal' : 1.0,
        'vs_fighting' : 0.5,
        'vs_flying' : 0.5,
        'vs_poison' : 0.5,
        'vs_ground' : 1.0,
        'vs_rock' : 1.0,
        'vs_bug' : 1.0,
        'vs_ghost' : 0.5,
        'vs_steel' : 0.5,
        'vs_fire' : 0.5,
        'vs_water' : 1.0,
        'vs_grass' : 2.0,
        'vs_electric' : 1.0,
        'vs_psychic' : 2.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 2.0,
        'vs_fairy' : 0.5,
        'id' : 7
    },
    'ghost': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'physical',
        'identifier' : 'ghost',
        'vs_normal' : 0.0,
        'vs_fighting' : 1.0,
        'vs_flying' : 1.0,
        'vs_poison' : 1.0,
        'vs_ground' : 1.0,
        'vs_rock' : 1.0,
        'vs_bug' : 1.0,
        'vs_ghost' : 2.0,
        'vs_steel' : 1.0,
        'vs_fire' : 1.0,
        'vs_water' : 1.0,
        'vs_grass' : 1.0,
        'vs_electric' : 1.0,
        'vs_psychic' : 2.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 1.0,
        'vs_dark' : 0.5,
        'vs_fairy' : 1.0,
        'id' : 8

    },
    'steel': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'physical',
        'identifier': 'steel',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 2.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 0.5,
        'vs_water': 0.5,
        'vs_grass': 1.0,
        'vs_electric': 0.5,
        'vs_psychic': 1.0,
        'vs_ice': 2.0,
        'vs_dragon': 1.0,
        'vs_dark': 1.0,
        'vs_fairy': 2.0,
        'id': 9
    },
    'fire': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'fire',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 0.5,
        'vs_bug': 2.0,
        'vs_ghost': 1.0,
        'vs_steel': 2.0,
        'vs_fire': 0.5,
        'vs_water': 0.5,
        'vs_grass': 2.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 2.0,
        'vs_dragon': 0.5,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 10
    },
    'grass': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class' : 'special',
        'identifier' : 'grass',
        'vs_normal' : 1.0,
        'vs_fighting' : 1.0,
        'vs_flying' : 0.5,
        'vs_poison' : 0.5,
        'vs_ground' : 2.0,
        'vs_rock' : 2.0,
        'vs_bug' : 0.5,
        'vs_ghost' : 1.0,
        'vs_steel' : 0.5,
        'vs_fire' : 0.5,
        'vs_water' : 2.0,
        'vs_grass' : 0.5,
        'vs_electric' : 1.0,
        'vs_psychic' : 1.0,
        'vs_ice' : 1.0,
        'vs_dragon' : 0.5,
        'vs_dark' : 1.0,
        'vs_fairy' : 1.0,
        'id' : 12
    },
    'electric': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'electric',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 2.0,
        'vs_poison': 1.0,
        'vs_ground': 0.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 1.0,
        'vs_fire': 1.0,
        'vs_water': 2.0,
        'vs_grass': 0.5,
        'vs_electric': 0.5,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 0.5,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 13
    },
    'psychic': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'psychic',
        'vs_normal': 1.0,
        'vs_fighting': 2.0,
        'vs_flying': 1.0,
        'vs_poison': 2.0,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 0.5,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 0.0,
        'vs_fairy': 1.0,
        'id': 14
    },
    'ice': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'ice',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 2.0,
        'vs_poison': 1.0,
        'vs_ground': 2.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 0.5,
        'vs_water': 0.5,
        'vs_grass': 2.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 0.5,
        'vs_dragon': 2.0,
        'vs_dark': 1.0,
        'vs_fairy': 1.0,
        'id': 15
    },
    'dragon': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'dragon',
        'vs_normal': 1.0,
        'vs_fighting': 1.0,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 2.0,
        'vs_dark': 1.0,
        'vs_fairy': 0.0,
        'id': 16
    },
    'dark': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': 'special',
        'identifier': 'dark',
        'vs_normal': 1.0,
        'vs_fighting': 0.5,
        'vs_flying': 1.0,
        'vs_poison': 1.0,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 2.0,
        'vs_steel': 1.0,
        'vs_fire': 1.0,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 2.0,
        'vs_ice': 1.0,
        'vs_dragon': 1.0,
        'vs_dark': 0.5,
        'vs_fairy': 0.5,
        'id': 17

    },
    'fairy': {
        'info': '',
        'info2': '',
        'image': '',
        'advantages': '',
        'weaknesses': '',
        'pokemon': '',
        'damage_class': '',
        'identifier': 'fairy',
        'vs_normal': 1.0,
        'vs_fighting': 2.0,
        'vs_flying': 1.0,
        'vs_poison': 0.5,
        'vs_ground': 1.0,
        'vs_rock': 1.0,
        'vs_bug': 1.0,
        'vs_ghost': 1.0,
        'vs_steel': 0.5,
        'vs_fire': 0.5,
        'vs_water': 1.0,
        'vs_grass': 1.0,
        'vs_electric': 1.0,
        'vs_psychic': 1.0,
        'vs_ice': 1.0,
        'vs_dragon': 2.0,
        'vs_dark': 2.0,
        'vs_fairy': 1.0,
        'id': 18

    }


}
