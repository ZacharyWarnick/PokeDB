"""Creates the database from cached JSON files."""

import json

from collections import defaultdict
from models import db
from models import Pokemon, Type, BaseStats, Form, Evolution
from pathlib import Path
from config import DefaultConfig


def load_json(fname):
    fpath = Path(DefaultConfig.TABLE_DATA_DIR) / '{}.json'.format(fname)
    if not fpath.exists():
        raise FileNotFoundError('File doesn\'t exist:', fpath)

    with fpath.open(errors="ignore") as f:
        return json.load(f)


def create_stats():
    base_stats = load_json('base_stats')

    for b in base_stats:
        new_stats = BaseStats(
            variant_id=b['variant_id'],
            hp=b['hp'],
            attack=b['attack'],
            defense=b['defense'],
            special_attack=b['special-attack'],
            special_defense=b['special-defense'],
            speed=b['speed']
            )

        db.session.add(new_stats)
        db.session.commit()


def create_form():
    forms = load_json('forms')

    for f in forms:
        new_form = Form(
            id=f['id'],
            identifier=f['identifier'],
            pokemon_id=f['pokemon_id'],
            variant_id=f['variant_id'],
            pokemon_name=f['pokemon_name'],
            form_label=f['form_label'],
            first_type_id=f['first_type_id'],
            second_type_id=f['second_type_id'],
            alt_sprite=f.get('alt_sprite', None),
            alt_image=f.get('alt_image', None)
            )

        db.session.add(new_form)
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
            second_type_id=p['second_type_id'],
            flavor_text=p['flavor_text'],
            has_alt_form=p['has_alt_form'],
            sprite=p['sprite'],
            image=p['image']
            )

        db.session.add(new_pokemon)
        db.session.commit()


def create_evolution():
    evolution = load_json('evolutions')

    for evo in evolution:
        e = defaultdict(lambda: None)
        e.update(evo)

        new_evo = Evolution(
            id=e['id'],
            evolves_from_pokemon_id=e['evolves_from_pokemon_id'],
            pokemon_id=e['pokemon_id'],
            evolution_chain_id=e['evolution_chain_id'],
            trigger=e['trigger'],
            level=e['level'],
            difficulty=e['difficulty'],
            happiness=e['happiness'],
            trigger_item=e['trigger_item'],
            relative_stats=e['relative_stats'],
            held_item=e['held_item'],
            time_of_day=e['time_of_day'],
            known_move=e['known_move'],
            party_pokemon_id=e['party_pokemon_id'],
            beauty=e['beauty'],
            gender=e['gender'],
            location=e['location'],
            trade_pokemon_id=e['trade_pokemon_id'],
            needs_inversion=e['needs_inversion'],
            party_type_id=e['party_type_id'],
            needs_rain=e['needs_rain'],
            known_move_type_id=e['known_move_type_id'],
            affection=e['affection']
            )

        db.session.add(new_evo)
        db.session.commit()


def initialize():
    create_type()
    create_pokemon()
    create_evolution()
    create_stats()
    create_form()


def reset():
    for table in ['pokemon', 'type', 'evolution', 'form', 'base_stats']:
        db.engine.execute('DROP TABLE if exists {} cascade;'.format(table))

    db.engine.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    db.create_all()
