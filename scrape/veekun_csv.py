"""Parses CSV files from Veekun's Pokédex to build a JSON database.

The JSON is a precursor to building a PostgreSQL database.

Pokédex Repository: https://github.com/veekun/pokedex
"""

import csv
import json

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
    'item_names': ['item_id', 'local_language_id', 'name'],
    'location_names': ['location_id', 'local_language_id', 'name', 'subtitle'],
    'locations': ['id', 'region_id', 'identifier'],
    'move_damage_classes': ['id', 'identifier'],
    'move_names': ['move_id', 'local_language_id', 'name'],
    'pokemon_colors': ['id', 'identifier'],
    'pokemon_evolution': [
        'id', 'evolved_species_id', 'evolution_trigger_id', 'trigger_item_id',
        'minimum_level', 'gender_id', 'location_id', 'held_item_id',
        'time_of_day', 'known_move_id', 'known_move_type_id',
        'minimum_happiness', 'minimum_beauty', 'minimum_affection',
        'relative_physical_stats', 'party_species_id', 'party_type_id',
        'trade_species_id', 'needs_overworld_rain', 'turn_upside_down'
    ],
    'pokemon_forms': [
        'id', 'identifier', 'form_identifier', 'pokemon_id', 'form_order'
    ],
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
    'region_names': ['region_id', 'local_language_id', 'name'],
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


def _int(x): return int(x) if bool(x) else None


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
        self.out = Path(out_dir) if out_dir else None

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
            if (('local_language_id' in row)
                    and (int(row['local_language_id']) is not _LANG_EN)):
                continue
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
        region_names = self.simple_map('region_names', 'region_id', 'name')
        loc_regions = self.simple_map('locations', 'id', 'region_id')
        loc_regions = {k: int(v) for k, v in loc_regions.items() if v}

        loc_map = {
            'location_id': ('id', int),
            'id': ('id', int),
            'local_language_id': ('lang', int),
            **map_id(region_names, 'region_id', 'region')
        }

        sub_fmt = ' ({})'
        reg_fmt = ', {} Region'
        locations = defaultdict(dict)
        for row in self.csv_generator('location_names', maps=loc_map):
            if row['lang'] == _LANG_EN:
                row_id = row['id']

                has_sub = 'subtitle' in row and row['subtitle']
                sub = sub_fmt.format(row['subtitle']) if has_sub else ''
                has_reg = row_id in loc_regions
                reg_name = region_names[loc_regions[row_id]] if has_reg else ''
                region = reg_fmt.format(reg_name) if reg_name else ''
                loc_name = row['name'] + sub + region

                locations[row_id]['name'] = loc_name

        self.locations = locations

    def parse_types(self):
        damage_classes = self.simple_map('move_damage_classes')

        def convert_scale(x: str):
            return int(x) / 100

        types = defaultdict(dict)
        type_tf = {
            'id': (int,),
            **map_id(damage_classes, 'damage_class_id', 'damage_class')
        }
        for row in self.csv_generator('types', maps=type_tf):
            if row['id'] >= 10000:
                continue

            new_type = types[row['id']]
            copy_fields(self.type_fields, src=row, dest=new_type)

        eff_tf = {
            'damage_type_id': ('id', int),
            'target_type_id': ('target', int),
            'damage_factor': ('factor', convert_scale)
        }

        for row in self.csv_generator('type_efficacy', maps=eff_tf):
            type_info = types[row['id']]
            defender_key = 'vs_' + types[row['target']]['identifier']
            type_info[defender_key] = row['factor']

        self.types = types

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
            'form_identifier': ('form_identifier', str),
            'form_order': (int,),
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
            form_identifier = row['form_identifier']
            if form_identifier:
                name = row['identifier']
                type1 = None
                poke_name = None
                form_label = None

                # The forms for these aren't properly supported in the CSV.
                # The special case is being handled explicitly.
                if name.startswith('arceus') or name.startswith('silvally'):
                    for k, v in self.types.items():
                        type_name = v['identifier']
                        if type_name == row['form_identifier']:
                            form_label = type_name.capitalize() + ' Type'
                            parts = reversed(name.split('-'))
                            poke_name = ' '.join(map(str.capitalize, parts))
                            type1 = k
                            break

                    # Found an unsupported type, skip the row.
                    if type1 is None:
                        continue

                if row_id in form_details:
                    detail = form_details[row_id]
                    poke_name = detail['name']
                    form_label = detail['label']

                new_form = forms[row_id]
                new_form['identifier'] = form_identifier
                new_form['pokemon_id'] = simple_pokemon[spec_id]
                new_form['pokemon_variant'] = spec_id
                new_form['pokemon_name'] = poke_name
                new_form['form_label'] = form_label

                if type1 is not None:
                    new_form['type1'] = type1

                new_form['pokemon_name'] = poke_name

                types = poke_types[spec_id]
                copy_fields(self.poke_type_fields, src=types, dest=new_form)

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
            poke = pokemon[key]
            poke['has_alt_form'] = has_alt

        self.pokemon = pokemon
        self.forms = forms
        self.base_stats = stats

    def parse_evolutions(self):
        if not self.pokemon:
            self.parse_pokemon()

        triggers = self.simple_map('evolution_triggers')
        items = self.simple_map('item_names', 'item_id', 'name')
        genders = self.simple_map('genders')
        moves = self.simple_map('move_names', 'move_id', 'name')

        poke_tf = {
            'id': (int,),
            'evolved_species_id': ('evolved_species', int),
            'minimum_level': ('level', _int),
            'minimum_happiness': ('happiness', _int),
            'minimum_beauty': ('beauty', _int),
            'minimum_affection': ('affection', _int),
            'relative_physical_stats': ('relative_stats', _int),
            'needs_overworld_rain': ('needs_rain', _bool),
            'turn_upside_down': ('needs_inversion', _bool),
            'known_move_type_id': ('known_move_type', _int),
            'party_type_id': ('party_type', _int),
            'party_species_id': ('party_pokemon', _int),
            'trade_species_id': ('trade_pokemon', _int),
            'location_id': ('location', _int),
            **map_id(items, 'trigger_item_id', 'trigger_item'),
            **map_id(triggers, 'evolution_trigger_id', 'trigger'),
            **map_id(genders, 'gender_id', 'gender'),
            **map_id(items, 'held_item_id', 'held_item'),
            **map_id(moves, 'known_move_id', 'known_move'),
        }

        stages = defaultdict(dict)
        for row in self.csv_generator('pokemon_evolution', maps=poke_tf):
            end = row['evolved_species']
            start = self.pokemon[end]
            start_id = start['evolves_from']
            chain_id = start['evolution_chain']

            stage = stages[row['id']]
            stage['evolves_from'] = start_id
            stage['result'] = end
            stage['chain'] = chain_id
            for key, value in row.items():
                if key in {'id', 'evolved_species', ''}:
                    continue

                if value in {None, '', False}:
                    continue

                if key == 'location':
                    loc = self.locations[value]
                    stage[key] = loc['name']
                    continue

                stage[key] = value

        final_stages = dict()
        for k, v in stages.items():
            if len(v) == 4 and v['trigger'] == 'level-up':
                pprint(v)
                continue

            final_stages[k] = v

        self.evolutions = final_stages

        for key in self.pokemon:
            chain_id = self.pokemon[key]['evolution_chain']

            chain_count = 0
            for ev in self.evolutions.values():
                if ev['chain'] == chain_id:
                    chain_count += 1

            poke = self.pokemon[key]
            if chain_count < 1 and poke['evolution_chain'] is not None:
                print(poke['name'], poke['evolution_chain'])
                poke['evolution_chain'] = None

    def run(self, pretty=False):
        self.parse_locations()
        self.parse_types()
        self.parse_pokemon()
        self.parse_evolutions()

        if not self.out:
            print('Skipping output, no path provided!')
            return
        elif not self.out.is_dir():
            self.out.mkdir(parents=True)

        file_names = [
            'pokemon', 'forms',
            'evolutions',
            'types', 'base_stats'
        ]

        objects = [
            self.pokemon, self.forms,
            self.evolutions,
            self.types, self.base_stats
        ]

        for fname, obj in zip(file_names, objects):
            path = self.out / '{}.json'.format(fname)
            indent = None if not pretty else 4
            rows = []
            for k, v in obj.items():
                row = v.copy()
                row['id'] = k
                rows.append(row)

            with path.open(mode='w+') as f:
                json.dump(rows, f, indent=indent, ensure_ascii=False)
                print('Saved:', path)

    def debug_print(self, poke_id):
        poke = self.pokemon[poke_id]
        pre_poke = poke['evolves_from']
        if pre_poke is not None:
            pprint(self.pokemon[pre_poke])

        pprint(poke)

        evolution_chain = poke['evolution_chain']

        whole_chain = []
        for k, v in self.evolutions.items():
            if v['chain'] == evolution_chain:
                whole_chain.append((k, v))

        pprint(sorted(whole_chain))

        if pre_poke is not None:
            pprint(self.base_stats[pre_poke])
        pprint(self.base_stats[poke_id])

        type_id = poke['type1']
        type_id_2 = poke['type2']
        pprint(self.types[type_id])
        if type_id_2:
            pprint(self.types[type_id_2])


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser('Veekun CSV Parser')
    parser.add_argument('--dir', '-d', help='The csv source directory.')
    parser.add_argument('--out', '-o', help='The output directory.')
    parser.add_argument(
        '--debug', help='Prints info for a pokemon for debugging.', type=int)
    parser.add_argument('--pretty',
                        help='Causes output json to be pretty-printed.',
                        action='store_true')
    args = parser.parse_args()

    session = Session(args.dir, args.out)
    session.run(pretty=args.pretty)

    if args.debug is not None:
        session.debug_print(args.debug)
