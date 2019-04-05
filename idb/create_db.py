import json

"""Creates the database from cached JSON files."""

from models import app, db
from models import Pokemon, Type, BaseStats
from pathlib import Path

_THIS_DIR = Path(__file__).parent
TARGET_DIR = _THIS_DIR.parent / 'scrape' / 'out'


def load_json(fname):
    fpath = TARGET_DIR / '{}.json'.format(fname)
    if not fpath.exists():
        print(fpath)

    with fpath.open() as f:
        return json.load(f)


def create_stats():
    base_stats = load_json('base_stats')

    for b in base_stats:
        new_stats = BaseStats(
            pokemon_id=b['pokemon_id'],
            hp=b['hp'],
            attack=b['attack'],
            defense=b['defense'],
            special_attack=b['special-attack'],
            special_defense=b['special-defense'],
            speed=b['speed']
        )

        db.session.add(new_stats)
        db.session.commit()


def create_type():
    types = load_json('types')

    for t in types:
        new_type = Type(
            id=t['id'],
            damage_class=t['damage_class'],
            identifier=t['identifier'],
            vs_normal=t['vs_normal'],
            vs_fighting=t['vs_fighting'],
            vs_flying=t['vs_flying'],
            vs_poison=t['vs_poison'],
            vs_ground=t['vs_ground'],
            vs_rock=t['vs_rock'],
            vs_bug=t['vs_bug'],
            vs_ghost=t['vs_ghost'],
            vs_steel=t['vs_steel'],
            vs_fire=t['vs_fire'],
            vs_water=t['vs_water'],
            vs_grass=t['vs_grass'],
            vs_electric=t['vs_electric'],
            vs_psychic=t['vs_psychic'],
            vs_ice=t['vs_ice'],
            vs_dragon=t['vs_dragon'],
            vs_dark=t['vs_dark'],
            vs_fairy=t['vs_fairy'],
            pokemon_count=t['pokemon_count'],
            stat_average=t['stat_average'],
            relative_advantage=t['relative_advantage'],
            desc_info=t['desc_info'],
            desc_atk=t['desc_atk'],
            desc_def=t['desc_def']
        )

        db.session.add(new_type)
        db.session.commit()


def create_pokemon():
    pokemon = load_json('pokemon')

    for p in pokemon:
        new_pokemon = Pokemon(
            id=p['id'],
            name=p['name'],
            genus=p['genus'],
            identifier=p['identifier'],
            evolution_chain_id=p['evolution_chain_id'],
            color=p['color'],
            since_gen=p['since_gen'],
            evolves_from_pokemon_id=p['evolves_from_pokemon_id'],
            first_type_id=p['first_type_id'],
            flavor_text=p['flavor_text'],
            has_alt_form=p['has_alt_form'],
            sprite=p['sprite'],
            image=p['image']
        )

        db.session.add(new_pokemon)
        db.session.commit()


if __name__ == '__main__':
    create_type()
    create_pokemon()
    create_stats()
