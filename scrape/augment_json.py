"""Adds fields to JSON scraped by veekun_csv.py."""

import json
import requests

from multiprocessing import Pool
from pathlib import Path


SPRITE_URL_FMT = "https://github.com/ymin1103/sprites/tree/sprite803-807/sprites/pokemon/{}.png"  # noqa: E501


def read_json(fpath):
    with fpath.open() as f:
        return json.load(f)


def sprite_url(*args):
    name = '-'.join(map(str, args))
    return SPRITE_URL_FMT.format(name)


def is_dead_url(url):
    request = requests.get(url)
    return request.status_code == 404


def find_form_sprite(form):
    form_id = form['id']
    identifier = form['identifier']

    poke_id = form['pokemon_id'] if 'pokemon_id' in form else form_id
    variant = form['pokemon_variant'] if 'pokemon_variant' in form else form_id

    test_url = None
    if poke_id == variant:
        test_url = sprite_url(poke_id)
    else:
        test_url = sprite_url(poke_id, identifier)

    if is_dead_url(test_url):
        test_url = sprite_url(variant)
        if is_dead_url(test_url):
            return (form_id, None)

    return (form_id, test_url)


def check_sprites(data, pool=None):
    if pool:
        sprite_info = pool.imap(find_form_sprite, data)
    else:
        sprite_info = map(find_form_sprite, data)

    n_forms = len(data)

    form_info = []
    for i, f in enumerate(sprite_info):
        print('\rCompleted:', i + 1, '/', n_forms, end='')
        form_info.append(f)

    print()
    return form_info


class Session(object):

    def __init__(self, src_dir, out_dir):
        self.out = Path(out_dir) if out_dir else None

        source = Path(src_dir)
        self.forms = read_json(source / 'forms.json')
        self.pokemon = read_json(source / 'pokemon.json')
        self.types = read_json(source / 'types.json')
        self.evolutions = read_json(source / 'evolutions.json')

    def augment_forms(self, pool=None):
        form_info = check_sprites(self.forms, pool)
        print(list(filter(lambda t: t[1] is None, form_info)))

    def augment_pokemon(self, pool=None):
        form_info = check_sprites(self.pokemon, pool)
        print(list(filter(lambda t: t[1] is None, form_info)))

    def augment_types(self):
        pass

    def augment_evolutions(self):
        pass


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser('Veekun JSON Augmentation')
    parser.add_argument('--dir', '-d', help='The json source directory.')
    parser.add_argument('--out', '-o', help='The output directory.')
    parser.add_argument('--pretty',
                        help='Causes output json to be pretty-printed.',
                        action='store_true')
    args = parser.parse_args()

    session = Session(args.dir, None)

    with Pool(processes=32) as pool:
        # session.augment_forms(pool)
        session.augment_pokemon(pool)
