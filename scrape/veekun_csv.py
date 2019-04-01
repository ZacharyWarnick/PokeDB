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
    'location_names': ['location_id', 'local_language_id', 'name', 'subtitle'],
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
    'pokemon_forms': ['id', 'identifier', 'form_identifier', 'pokemon_id'],
    'pokemon_form_names': [
        'pokemon_form_id', 'local_language_id', 'form_name', 'pokemon_name'
    ],
    'pokemon_habitats': ['id', 'identifier'],
    'pokemon_species_flavor_text': [
        'species_id', 'version_id', 'language_id', 'flavor_text'
    ],
    'pokemon_species_names': [
        'pokemon_species_id', 'local_language_id', 'name', 'genus'
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


def new_type_container():
    return {'type1': None, 'type2': None}


def form_detail(form_id, modifier, name):
    return {'id': form_id, 'modifier': modifier, 'name': name}


def copy_fields(fields, src, dest):
    for key in fields:
        dest[key] = src[key]


class Session(object):

    def __init__(self, csv_dir, out_dir):
        self.root = Path(csv_dir)
        self.out = Path(out_dir)

        self.pokemon = {}
        self.evolutions = {}
        self.types = {}
        self.forms = {}
        self.base_stats = {}
        self.stages = {}

        self.name_fields = ['name', 'genus']
        self.species_fields = [
            'identifier', 'evolution_chain', 'color', 'since_gen',
            'evolves_from'
        ]
        self.type_fields = ['damage_class', 'identifier']
        self.poke_type_fields = ['type1', 'type2']
        self.form_fields = ['label', 'name']

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

    def read_species_text(self):
        species_text = defaultdict(dict)
        map_desc = {
            'pokemon_species_id': (int,),
            'species_id': (int,),
            'language_id': (int,),
            'local_language_id': (int,),
            'version_id': (int,)
        }
        for row in self.csv_generator('pokemon_species_names', maps=map_desc):
            if row['local_language_id'] == _LANG_EN:
                current_data = species_text[row['pokemon_species_id']]
                copy_fields(self.name_fields, src=row, dest=current_data)

        map_desc['name'] = ('identifier', str)
        for row in self.csv_generator('pokemon_species_flavor_text',
                                      maps=map_desc):
            if ((row['language_id'] == _LANG_EN)
                    and (row['version_id'] >= _FLAVOR_VERSION)):
                poke_id = row['species_id']
                species_text[poke_id]['flavor_text'] = row['flavor_text']

        return species_text

    def parse_locations(self):
        location_info = self.simple_map('locations')

        loc_map = {
            'location_id': ('id', int),
            'local_language_id': ('lang', int)
        }

        locations = defaultdict(dict)
        for row in self.csv_generator('location_names', maps=loc_map):
            if row['lang'] == _LANG_EN:
                row_id = row['id']
                locations[row_id]['name'] = row['name']
                locations[row_id]['subtitle'] = row['subtitle']
                locations[row_id]['identifier'] = location_info[row_id]

        self.locations = locations

    def parse_types(self):
        damage_classes = self.simple_map('move_damage_classes')

        def convert_scale(x: str):
            return int(x) / 100

        type_info = defaultdict(dict)
        type_tf = {
            'id': (int,),
            **map_id(damage_classes, 'damage_class_id', 'damage_class')
        }
        for row in self.csv_generator('types', maps=type_tf):
            new_type = type_info[row['id']]
            copy_fields(self.type_fields, src=row, dest=new_type)

        self.types = type_info

    def parse_pokemon(self):
        colors = self.simple_map('pokemon_colors')
        stat_names = self.simple_map('stats')
        species_text = self.read_species_text()

        form_tf = {
            'pokemon_form_id': ('id', int),
            'local_language_id': ('lang', int),
            'form_name': ('label', str),
            'pokemon_name': ('name', str)
        }
        form_details = defaultdict(dict)
        for row in self.csv_generator('pokemon_form_names', maps=form_tf):
            if row['lang'] == _LANG_EN and (row['label'] or row['name']):
                new_detail = form_details[row['id']]
                copy_fields(self.form_fields, src=row, dest=new_detail)

        poke_tf = {
            'id': (int,),
            'pokemon_id': (int,),
            'species_id': (int,),
            'generation_id': ('since_gen', int),
            'type_id': ('type', int),
            'base_stat': (int,),
            'slot': (_int,),
            'evolves_from_species_id': ('evolves_from', _int),
            'evolution_chain_id': ('evolution_chain', int),
            'is_default': (_bool,),
            'form_identifier': ('identifier', str),
            **map_id(colors, 'color_id', 'color'),
            **map_id(stat_names, 'stat_id', 'stat')
        }

        species = defaultdict(dict)
        for row in self.csv_generator('pokemon_species', maps=poke_tf):
            spec = species[row['id']]
            copy_fields(self.species_fields, src=row, dest=spec)

        poke_types = defaultdict(new_type_container)
        for row in self.csv_generator('pokemon_types', maps=poke_tf):
            poke_info = poke_types[row['pokemon_id']]
            if row['slot'] is not None:
                key = 'type{}'.format(row['slot'])
                poke_info[key] = row['type']

        stats = defaultdict(dict)
        for row in self.csv_generator('pokemon_stats', maps=poke_tf):
            stats[row['pokemon_id']][row['stat']] = row['base_stat']

        simple_pokemon = {}
        for row in self.csv_generator('pokemon', maps=poke_tf):
            simple_pokemon[row['id']] = row['species_id']

        forms = defaultdict(dict)
        for row in self.csv_generator('pokemon_forms', maps=poke_tf):
            row_id = row['id']
            spec_id = row['pokemon_id']
            identifier = row['identifier']
            if identifier and (row_id in form_details):
                detail = form_details[row_id]
                new_form = forms[row_id]
                new_form['pokemon_name'] = detail['name']
                new_form['form_label'] = detail['label']
                new_form['identifier'] = identifier
                new_form['pokemon_id'] = simple_pokemon[row['pokemon_id']]

        pokemon = defaultdict(dict)
        for row in self.csv_generator('pokemon', maps=poke_tf):
            spec_id = row['species_id']
            row_id = row['id']

            poke = pokemon[spec_id]
            spec = species[spec_id]

            if row['is_default']:
                text_info = species_text[spec_id]
                type_info = poke_types[row_id]
                copy_fields(self.name_fields, src=text_info, dest=poke)
                copy_fields(self.species_fields, src=spec, dest=poke)
                copy_fields(self.poke_type_fields, src=type_info, dest=poke)
                poke['flavor_text'] = species_text[spec_id]['flavor_text']

        for key in pokemon:
            has_alt = key in forms
            pokemon[key]['has_alt_form'] = has_alt

        self.pokemon = pokemon
        self.forms = forms
        self.base_stats = stats

    def parse_evolutions(self):
        if not self.pokemon:
            self.parse_pokemon()

        triggers = self.simple_map('evolution_triggers')
        items = self.simple_map('items')
        genders = self.simple_map('genders')
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
            'location_id': ('location', _int),
            **map_id(items, 'trigger_item_id', 'trigger_item'),
            **map_id(triggers, 'evolution_trigger_id', 'trigger'),
            **map_id(genders, 'gender_id', 'gender'),
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

            chains[chain_id].append(row['id'])

        self.stages = stages
        self.evolutions = chains

        for key in self.pokemon:
            chain_id = self.pokemon[key]['evolution_chain']

            if not self.evolutions.get(chain_id, None):
                self.pokemon[key]['evolution_chain'] = None

    def debug_print(self):
        eevee_id = 133
        eevee_chain = 67
        eeveelution_stages = [
            76, 77, 78, 109, 110, 238, 239, 324, 325, 361, 363, 364, 368, 369
        ]
        malie_city_cape_id = 798
        battle_bond_greninja_id = 10218

        pprint(self.pokemon[eevee_id])
        pprint(self.evolutions[eevee_chain])
        pprint([self.stages[i] for i in eeveelution_stages])
        pprint(self.locations[malie_city_cape_id])
        pprint(self.forms[battle_bond_greninja_id])
        pprint(self.base_stats[eevee_id])


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser('Veekun CSV Parser')
    parser.add_argument('--dir', '-d', help='The csv source directory.')
    args = parser.parse_args()

    session = Session(args.dir, '')
    session.parse_locations()
    session.parse_types()
    session.parse_pokemon()
    session.parse_evolutions()

    session.debug_print()
