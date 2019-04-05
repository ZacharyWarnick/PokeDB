
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DatabaseConfig

app = Flask(__name__)
app.config.from_object(DatabaseConfig)

db = SQLAlchemy(app)


def fkey(k): return db.ForeignKey(k)


class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    # Integers
    id = db.Column(db.Integer, primary_key=True)
    evolution_chain_id = db.Column(db.Integer)
    evolves_from_pokemon_id = db.Column(db.Integer)
    since_gen = db.Column(db.Integer)
    first_type_id = db.Column(db.Integer, fkey('type.id'), nullable=False)
    second_type_id = db.Column(db.Integer, fkey('type.id'))

    # Strings
    name = db.Column(db.String(15), unique=True, nullable=False)
    genus = db.Column(db.String(25), nullable=False)
    identifier = db.Column(db.String(12), unique=True, nullable=False)
    color = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(125), nullable=False)
    sprite = db.Column(db.String(85), nullable=False)
    flavor_text = db.Column(db.String(250))

    # Boolean
    has_alt_form = db.Column(db.Boolean)

    def __repr__(self):
        return '{name} ({id})'.format(
            name=self.name, id=self.id
        )


class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    damage_class = db.Column(db.String(10), nullable=False)
    identifier = db.Column(db.String(10), unique=True, nullable=False)
    vs_normal = db.Column(db.Float)
    vs_fighting = db.Column(db.Float)
    vs_flying = db.Column(db.Float)
    vs_poison = db.Column(db.Float)
    vs_ground = db.Column(db.Float)
    vs_rock = db.Column(db.Float)
    vs_bug = db.Column(db.Float)
    vs_ghost = db.Column(db.Float)
    vs_steel = db.Column(db.Float)
    vs_fire = db.Column(db.Float)
    vs_water = db.Column(db.Float)
    vs_grass = db.Column(db.Float)
    vs_electric = db.Column(db.Float)
    vs_psychic = db.Column(db.Float)
    vs_ice = db.Column(db.Float)
    vs_dragon = db.Column(db.Float)
    vs_dark = db.Column(db.Float)
    vs_fairy = db.Column(db.Float)
    pokemon_count = db.Column(db.Integer)
    stat_average = db.Column(db.Integer)
    relative_advantage = db.Column(db.Float)
    desc_info = db.Column(db.String(550))
    desc_atk = db.Column(db.String(850))
    desc_def = db.Column(db.String(850))


class Evolution(db.Model):
    __tablename__ = 'evolution'

    id = db.Column(db.Integer, primary_key=True)
    evolves_from_pokemon_id = db.Column(db.Integer, fkey('pokemon.id'))
    pokemon_id = db.Column(db.Integer, fkey('pokemon.id'))
    evolution_chain_id = db.Column(db.Integer)
    trigger = db.Column(db.String(10))
    level = db.Column(db.Integer)
    difficulty = db.Column(db.Float)
    happiness = db.Column(db.Integer)
    trigger_item = db.Column(db.String(15))
    relative_stats = db.Column(db.Integer)
    held_item = db.Column(db.String(20))
    time_of_day = db.Column(db.String(10))
    known_move = db.Column(db.String(15))
    party_pokemon_id = db.Column(db.Integer, fkey('pokemon.id'))
    beauty = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    location = db.Column(db.String(35))
    trade_pokemon_id = db.Column(db.Integer, fkey('pokemon.id'))
    needs_inversion = db.Column(db.Boolean)
    party_type_id = db.Column(db.Integer, fkey('type.id'))
    needs_rain = db.Column(db.Boolean)
    known_move_type_id = db.Column(db.Integer, fkey('type.id'))
    affection = db.Column(db.Integer)


class Form(db.Model):
    __tablename__ = 'form'

    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(20), unique=True)
    pokemon_id = db.Column(db.Integer, fkey('pokemon.id'))
    pokemon_variant_id = db.Column(db.Integer, unique=True)
    pokemon_name = db.Column(db.String(25))
    form_label = db.Column(db.String(25))
    first_type_id = db.Column(db.Integer, fkey('type.id'))
    second_type_id = db.Column(db.Integer, fkey('type.id'))
    alt_sprite = db.Column(db.String(100))
    alt_image = db.Column(db.String(130))


class BaseStats(db.Model):
    __tablename__ = 'base_stats'

    form_id = db.Column(db.Integer, fkey('form.id'), primary_key=True)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    special_attack = db.Column(db.Integer)
    special_defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)


for table in ['pokemon', 'type', 'evolution', 'form', 'base_stats']:
    db.engine.execute('DROP TABLE if exists {} cascade;'.format(table))
db.create_all()
