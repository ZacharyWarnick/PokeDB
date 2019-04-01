"""Parses CSV files from Veekun's Pokédex to build a JSON database.

The JSON is a precursor to building a PostgreSQL database.

Pokédex Repository: https://github.com/veekun/pokedex
"""

import csv

from collections import defaultdict
from pathlib import Path
from pprint import pprint

"""The integer ID value for English translations."""
_LANG_EN = 9

"""The preferred game from which to source flavor text."""
_FLAVOR_VERSION = 16  # Alpha Sapphire Version

"""The columns that will be parsed into python objects."""
_FIELDS = {
    'evolution_chains': ['id', 'identifier'],
    'evolution_triggers': ['id', 'identifier'],
    'genders': ['id', 'identifier'],
    'items': [
        'id', 'identifier', 'category_id'
    ],
    'locations': ['id', 'region_id', 'identifier'],
    'move_damage_classes': ['id', 'identifier'],
    'moves': ['id', 'identifier'],
    'pokemon_colors': ['id', 'identifier'],
    'pokemon_evolution': [
        'id', 'evolved_species_id', 'evolution_trigger_id', 'trigger_item_id',
        'minimum_level', 'gender_id', 'location_id', 'held_item_id',
        'time_of_day', 'known_move_id', 'known_move_type_id',
        'minimum_happiness', 'minimum_beauty', 'minimum_affection',
        'relative_physical_stats', 'party_species_id', 'party_type_id',
        'trade_species_id', 'needs_overworld_rain', 'turn_upside_down'
    ],
    'pokemon_habitats': ['id', 'identifier'],
    'pokemon_species_flavor_text': [
        'species_id', 'version_id', 'language_id', 'flavor_text'
    ],
    'pokemon_species': [
        'id', 'identifier', 'generation_id', 'evolves_from_species_id',
        'evolution_chain_id', 'color_id', 'shape_id',
        'is_baby', 'has_gender_differences', 'growth_rate_id',
        'forms_switchable'
    ],
    'pokemon_stats': ['pokemon_id', 'stat_id', 'base_stat', 'effort'],
    'pokemon_types': ['pokemon_id', 'type_id', 'slot'],
    'pokemon': [
        'id', 'identifier', 'species_id', 'order', 'is_default'
    ],
    'stats': [
        'id', 'damage_class_id', 'identifier'
    ],
    'type_efficacy': ['damage_type_id', 'target_type_id', 'damage_factor'],
    'types': ['id', 'identifier', 'generation_id', 'damage_class_id']
}


def map_id(source, old_key, new_key):
    """Converts id dictionary keys to the string identifier for the id."""
    def accessor(x): return x if not bool(x) else source[int(x)]
    return {old_key: (new_key, accessor)}


def try_cast(dtype):
    return lambda x: dtype(x) if bool(x) else None


_int = try_cast(int)


def _bool(x): return bool(int(x))


def new_poke():
    return {'types': [], 'forms': []}


def new_type_container():
    return [0]


def form_detail(form_id, modifier):
    return {'id': form_id, 'modifier': modifier}


class Session(object):

    def __init__(self, csv_dir, out_dir):
        self.root = Path(csv_dir)
        self.out = Path(out_dir)

        self.pokemon = {}
        self.evolutions = {}
        self.types = {}
        self.forms = {}
        self.base_stats = {}

    def csv_generator(self, fname, maps=None):
        with open(self.root / '{}.csv'.format(fname), newline='') as f:
            reader = csv.DictReader(f)

            for row in reader:
                for key in row.copy():
                    if key not in _FIELDS[fname]:
                        row.pop(key)

                if maps is None:
                    yield row
                    continue

                new_row = {}
                for key, value in row.items():
                    if key in maps:
                        itr = iter(maps[key])
                        if len(maps[key]) == 2:
                            key = next(itr)

                        new_row[key] = next(itr)(value)
                    else:
                        new_row[key] = value

                yield new_row

    def simple_map(self, name, id_key='id', name_key='identifier'):
        out = {}
        for row in self.csv_generator(name):
            out[int(row[id_key])] = row[name_key]

        return out

    def parse_types(self):
        damage_classes = self.simple_map('move_damage_classes')

        type_info = {}
        type_tf = map_id(damage_classes, 'damage_class_id', 'damage_class')
        for row in self.csv_generator('types', maps=type_tf):
            type_info[int(row['id'])] = {
                'name': row['identifier'],
                'damage_class': row['damage_class']
            }

        self.types = type_info

    def parse_pokemon(self):
        colors = self.simple_map('pokemon_colors')
        stat_names = self.simple_map('stats')

        poke_tf = {
            'id': (int,),
            'pokemon_id': (int,),
            'identifier': ('name', str),
            'species_id': (int,),
            'generation_id': ('since_gen', int),
            'type_id': ('type', int),
            'base_stat': (int,),
            'slot': (_int,),
            'evolves_from_species_id': ('evolves_from', _int),
            'evolution_chain_id': ('evolution_chain', int),
            'is_default': (_bool,),
            **map_id(colors, 'color_id', 'color'),
            **map_id(stat_names, 'stat_id', 'stat')
        }

        species = defaultdict(dict)
        for row in self.csv_generator('pokemon_species', maps=poke_tf):
            spec = species[row['id']]
            spec['name'] = row['name']
            spec['evolution_chain'] = row['evolution_chain']
            spec['color'] = row['color']
            spec['since_gen'] = row['since_gen']
            spec['evolves_from'] = row['evolves_from']

        poke_types = defaultdict(new_type_container)
        for row in self.csv_generator('pokemon_types', maps=poke_tf):
            poke_info = poke_types[row['pokemon_id']]
            slot_idx = row['slot'] - 1
            if slot_idx > 0:
                poke_info.append(row['type'])
            else:
                poke_info[slot_idx] = row['type']

        stats = defaultdict(dict)
        for row in self.csv_generator('pokemon_stats', maps=poke_tf):
            stats[row['pokemon_id']][row['stat']] = row['base_stat']

        pokemon = defaultdict(new_poke)
        forms = defaultdict(list)
        for row in self.csv_generator('pokemon', maps=poke_tf):
            spec_id = row['species_id']
            row_id = row['id']

            poke = pokemon[spec_id]
            spec = species[spec_id]

            form_name = None
            if not row['is_default']:
                split_point = row['name'].index('-') + 1
                form_name = row['name'][split_point:]

            forms[spec_id] += [form_detail(row_id, form_name)]

            if row['is_default']:
                poke['name'] = spec['name']
                poke['color'] = spec['color']
                poke['evolution_chain'] = spec['evolution_chain']
                poke['since_gen'] = spec['since_gen']
                poke['types'] = poke_types[row['id']]
                poke['evolves_from'] = spec['evolves_from']

        for key in forms.copy():
            if len(forms[key]) < 2:
                forms.pop(key)
            else:
                for form in forms[key]:
                    pokemon[key]['forms'] += [form['id']]

        self.pokemon = pokemon
        self.forms = forms
        self.base_stats = stats

    def parse_evolutions(self):
        if not self.pokemon:
            self.parse_pokemon()

        triggers = self.simple_map('evolution_triggers')
        items = self.simple_map('items')
        genders = self.simple_map('genders')
        locations = self.simple_map('locations')
        moves = self.simple_map('moves')
        types = self.simple_map('types')
        pokemon = self.simple_map('pokemon_species')

        poke_tf = {
            'id': (int,),
            'evolved_species_id': ('evolved_species', int),
            'minimum_level': ('level', _int),
            'minimum_happiness': ('happiness', _int),
            'minimum_beauty': ('beauty', _int),
            'relative_physical_stats': ('relative_stats', _int),
            'needs_overworld_rain': ('needs_rain', _bool),
            'turn_upside_down': ('needs_inversion', _bool),

            **map_id(items, 'trigger_item_id', 'trigger_item'),
            **map_id(triggers, 'evolution_trigger_id', 'trigger'),
            **map_id(genders, 'gender_id', 'gender'),
            **map_id(locations, 'location_id', 'location'),
            **map_id(items, 'held_item_id', 'held_item'),
            **map_id(moves, 'known_move_id', 'known_move'),
            **map_id(types, 'known_move_type_id', 'known_move_type'),
            **map_id(types, 'party_type_id', 'party_type'),
            **map_id(pokemon, 'party_species_id', 'party_species'),
            **map_id(pokemon, 'trade_species_id', 'trade_species'),
        }

        chains = defaultdict(list)
        stages = defaultdict(dict)
        for row in self.csv_generator('pokemon_evolution', maps=poke_tf):
            end = row['evolved_species']
            start = self.pokemon[end]
            start_id = start['evolves_from']
            chain_id = start['evolution_chain']

            stage = stages[row['id']]
            stage['evolves_from'] = start_id
            for key, value in row.items():
                if key in {'id', 'evolved_species', ''}:
                    continue
                
                if value in {None, '', False}:
                    continue
                
                stage[key] = value
            
            pprint(stage)
            chains[chain_id].append(row['id'])


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser('Veekun CSV Parser')
    parser.add_argument('--dir', '-d', help='The csv source directory.')
    args = parser.parse_args()

    session = Session(args.dir, '')
    session.parse_types()
    session.parse_pokemon()
    session.parse_evolutions()
