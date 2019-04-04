"""Adds fields to JSON scraped by veekun_csv.py."""

import json
import requests

from bs4 import BeautifulSoup
from functools import partial, wraps
from multiprocessing import Pool
from pathlib import Path
from pprint import pprint


SPRITE_URL_FMT = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png'  # noqa: E501
BACKUP_SPRITE_URL_FMT = 'https://github.com/ymin1103/sprites/tree/sprite803-807/sprites/pokemon/{}.png'  # noqa: E501

IMAGE_SOURCE_FMT = 'https://archives.bulbagarden.net/wiki/File:{id:0>3}{name}.png'  # noqa: E501


"""Specific Pokémon forms that have different URL identifiers."""
EXCEPTIONS = {
    # Specific form
    (421, 'sunshine'),
    (421, 'cherrim'),
    (666, 'poke-ball'),
    (741, 'pau'),
    (744, 'own-tempo'),
    (778, 'busted'),
    (658, 'battle-bond'),
    (586, 'sawsbuck'),
    (585, 'deerling'),
    (487, 'giratina'),
    (746, 'wishiwashi'),
    (741, 'oricorio'),
    (492, 'shaymin'),

    # All instances
    25, 29, 32, 83, 201, 493, 550, 649, 669, 670, 671, 676, 718, 773, 774, 800
}

NON_EXCEPTIONS = {
    (493, 'normal'),
    (649, 'normal')
}

NAME_ONLY = {
    414, 664, 665, 710, 711
}

DEFAULT_IDENTIFIERS = {
    'normal', 'incarnate', 'standard', 'average', 'ordinary', 'aria',
    'natural',
}

SKIPS_ID = {
    (172, 'spiky-eared'),
    (716, 'neutral'),
    (670, 'eternal'),
    (801, 'original')
}


def skip_gracefully(f):

    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyboardInterrupt:
            all_vals = [*args, *kwargs.values()]
            for a in all_vals:
                if isinstance(a, type(Pool)):
                    print('Found a pool!')
                    a.terminate()
                    a.join()
                    break
            
            print('\n')

    return wrapped


def handle_exception(poke_id, poke_name, identifier):
    if poke_id in NAME_ONLY:
        return poke_name

    if not identifier:
        return None
    elif identifier in DEFAULT_IDENTIFIERS:
        return poke_name

    if (poke_id, identifier) in NON_EXCEPTIONS:
        return None

    cap_id = identifier.capitalize()

    if poke_id == 201:
        return 'Unown_{}_Dream'.format(cap_id)

    if poke_id == 493:
        return 'Arceus_{}_Dream'.format(cap_id)

    if poke_id == 421:
        modifier = 'Sunny' if identifier == 'sunshine' else 'Overcast'
        return 'Cherrim-' + modifier

    if poke_id == 25:
        if cap_id.endswith('-cap'):
            return 'Pikachu-' + cap_id.replace('-cap', '')

        if identifier == 'phd':
            return 'Pikachu-PhD'

        if identifier == 'cosplay':
            return 'Pikachu'

    if 669 <= poke_id <= 671:
        if identifier == 'eternal':
            return 'AZ\'s_Floette'

        out = poke_name
        if identifier != 'red':
            out += '_{}_Flower_Dream'.format(cap_id)

        return out

    if poke_id == 649:
        return 'Genesect_{}_Dream'.format(cap_id[0])

    if poke_id == 773:
        return 'Silvally_{}_Dream'.format(cap_id)

    if poke_id == 774:
        if cap_id.endswith('meteor'):
            return poke_name
        else:
            return 'Minior_{}_Dream'.format(cap_id)

    if poke_id == 550:
        return poke_name + '-' + cap_id.replace('-striped', '')

    if poke_id == 172:
        return 'Spiky-eared_Pichu_DP_1'

    if poke_id == 676:
        spec = map(str.capitalize, identifier.split('-'))
        return 'Furfrou_{}_Dream'.format('_'.join(spec))

    if poke_id == 666:
        return 'Vivillon-Poké_Ball'

    if poke_id == 716:
        return 'Spr_6x_716N'

    if poke_id == 800:
        return 'Necrozma' + {
            'dawn': '-Dawn_Wings',
            'dusk': '-Dusk_Mane'
        }.get(identifier, '')

    if poke_id == 741:
        if identifier == 'oricorio':
            return 'Oricorio-Baile'
        return 'Oricorio-Pa\'u'

    if poke_id == 744:
        return 'Rockruff'

    if poke_id == 778:
        return 'Mimikyu_Busted_Dream'

    if poke_id == 801:
        return 'Spr_7s_801O'

    if poke_id == 718:
        return 'Zygarde' + {
            '10': '-10Percent',
            'complete': '-Complete'
        }.get(identifier, '')

    if poke_id == 658:
        return 'Greninja-Ash'

    if 585 <= poke_id <= 586:
        return poke_name + '-Spring'

    if poke_id in {29, 32}:
        return 'Nidoran'

    if poke_id == 83:
        return 'Farfetch\'d'

    if poke_id == 487:
        return 'Giratina-Altered'

    if poke_id == 746:
        return 'Wishiwashi-Solo'

    if poke_id == 492:
        return 'Shaymin-Land'


def read_json(fpath):
    with fpath.open() as f:
        return json.load(f)


def is_dead_url(url):
    request = requests.get(url)
    return request.status_code == 404


def sprite_url(*args, backup=False):
    name = '-'.join(map(str, args))
    fmt_string = SPRITE_URL_FMT if not backup else BACKUP_SPRITE_URL_FMT
    return fmt_string.format(name)


def image_url(poke_id, poke_name, skip_id=False):
    url = IMAGE_SOURCE_FMT.format(id=poke_id, name=poke_name)
    if skip_id:
        index = url.index(str(poke_id))
        url = url[:index] + url[index + 3:]

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    tag_alt = 'File:{:0>3}{}.png'.format(poke_id, poke_name.replace('_', ' '))
    if skip_id:
        index = tag_alt.index(str(poke_id))
        tag_alt = (tag_alt[:index] + tag_alt[index + 3:]).replace('_', ' ')

    img = soup.find('img', attrs={'alt': tag_alt})

    if img is None or 'src' not in img.attrs:
        if img:
            pprint(img.attrs)
        return None

    img_src = 'https:' + img.attrs['src']
    if is_dead_url(img_src):
        return None

    return img_src


def find_form_image(form, pokemon_names):
    form_id = form['id']
    identifier = form['identifier']

    poke_id = form['pokemon_id'] if 'pokemon_id' in form else form_id
    poke_name = pokemon_names[poke_id]

    exc_key = (poke_id, identifier)
    img = None
    if ((exc_key in EXCEPTIONS)
            or (poke_id in EXCEPTIONS)
            or (poke_id in NAME_ONLY)
            or (identifier in DEFAULT_IDENTIFIERS)
            or (exc_key in SKIPS_ID)):
        name = handle_exception(poke_id, poke_name, identifier)
        if name:
            skip_id = exc_key in SKIPS_ID
            img = image_url(poke_id, name, skip_id=skip_id)

    if img is not None:
        return (form_id, img)

    cap_words = list(map(str.capitalize, identifier.split('-')))
    if identifier.startswith('mega') and cap_words:
        name = '_'.join(cap_words)
        img = image_url(poke_id, '-'.join([poke_name, name]))

    if img is None and cap_words:
        name = '-'.join([poke_name, *cap_words])
        img = image_url(poke_id, name)

    if img is None and cap_words:
        name = '-'.join([poke_name, '_'.join(cap_words)])
        img = image_url(poke_id, name)

    if img is None and form_id == poke_id:
        img = image_url(poke_id, poke_name)

    if img is None and 'totem' in identifier:
        img = image_url(poke_id, poke_name)

    if img is None and poke_name:
        name = poke_name.replace(' ', '_').replace(':', '')
        name = name.replace('.', '')
        img = image_url(poke_id, name)

    if img is None:
        print(poke_id, poke_name, form_id, name, identifier)

    return (form_id, img)


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


def check_images(data, pokemon_names, pool=None):
    func = partial(find_form_image, pokemon_names=pokemon_names)
    if pool:
        image_info = pool.imap(func, data)
    else:
        image_info = map(func, data)

    n_forms = len(data)

    form_info = []
    for i, f in enumerate(image_info):
        print('\rCompleted:', i + 1, '/', n_forms, end='')
        form_info.append(f)

    print()
    return form_info


def add_sprites(targets, form_info, sprite_key, skip_default=False):
    bad_ids = []
    for poke_id, sprite in form_info:
        if sprite:
            form_index = -1
            for i, f in enumerate(targets):
                if f['id'] == poke_id:
                    form_index = i
                    break

            if form_index >= 0:
                selected_form = targets[form_index]
                if not (skip_default and is_default_form(selected_form)):
                    selected_form[sprite_key] = sprite
        else:
            bad_ids.append(poke_id)

    return bad_ids


def is_default_form(form):
    return form['pokemon_variant'] == form['id']


class Session(object):

    def __init__(self, src_dir, out_dir):
        self.out = Path(out_dir) if out_dir else None

        source = Path(src_dir)
        self.forms = read_json(source / 'forms.json')
        self.pokemon = read_json(source / 'pokemon.json')
        self.types = read_json(source / 'types.json')
        self.evolutions = read_json(source / 'evolutions.json')

        self.pokemon_names = {row['id']: row['name'] for row in self.pokemon}

    def augment_forms(self, pool=None):
        sprite_info = check_sprites(self.forms, pool)
        if not sprite_info:
            return

        image_info = check_images(self.forms, self.pokemon_names, pool)
        if not image_info:
            return

        bad_sprites = add_sprites(self.forms, sprite_info, 'alt_sprite',
                                  skip_default=True)

        bad_images = add_sprites(self.forms, image_info, 'alt_image',
                                 skip_default=True)

        for bad_id in bad_sprites:
            for f in self.forms:
                if f['id'] == bad_id:
                    f['alt_sprite'] = SPRITE_URL_FMT.format(f['pokemon_id'])

        print('Failed form sprites:')
        pprint(bad_sprites)

        print('Failed form images:')
        pprint(bad_images)

    def augment_pokemon(self, pool=None):
        form_info = check_sprites(self.pokemon, pool)
        if not form_info:
            return

        image_info = check_images(self.pokemon, self.pokemon_names, pool)
        if not image_info:
            return

        bad_sprites = add_sprites(self.pokemon, form_info, 'sprite',
                                  skip_default=False)

        bad_images = add_sprites(self.pokemon, image_info, 'image',
                                 skip_default=False)

        print('Failed poke sprites:')
        pprint(bad_sprites)

        print('Failed poke images:')
        pprint(bad_images)

    def augment_types(self):
        pass

    def augment_evolutions(self):
        pass

    def run(self, pool=None, pretty=False):

        @skip_gracefully
        def _run(pool):
            self.augment_forms(pool)
            self.augment_pokemon(pool)
            self.augment_evolutions()
            self.augment_types()

        _run(pool)

        if self.out is not None:
            if not self.out.exists():
                self.out.mkdir(parents=True)

            file_names = ['pokemon', 'forms', 'evolutions', 'types']
            objects = [self.pokemon, self.forms, self.evolutions, self.types]
            indent = None if not pretty else 4

            for fname, obj in zip(file_names, objects):
                path = self.out / '{}.json'.format(fname)

                if path.exists():
                    inp = input('File exists. Overwrite (N/y)?\t').lower()
                    if not inp or inp[0] == 'n':
                        continue

                with path.open(mode='w+') as f:
                    json.dump(obj, f, indent=indent, ensure_ascii=False)
                    print('Saved:', path)


if __name__ == '__main__':
    import signal
    from argparse import ArgumentParser

    def init_worker():
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    parser = ArgumentParser('Veekun JSON Augmentation')
    parser.add_argument('--dir', '-d', help='The json source directory.')
    parser.add_argument('--out', '-o', help='The output directory.')
    parser.add_argument('--pretty',
                        help='Causes output json to be pretty-printed.',
                        action='store_true')
    args = parser.parse_args()

    session = Session(args.dir, args.out)

    with Pool(32, init_worker) as pool:
        session.run(pool, pretty=args.pretty)
