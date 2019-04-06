from flask_sqlalchemy import SQLAlchemy

from model_base import create_base_model

db = SQLAlchemy()

# Alias these for convenience.
fkey = db.ForeignKey
rel = db.relationship

# Used to link a Pokémon's default form. Always yields a unique pair.
JOIN_POKE_FORM = 'and_(Pokemon.id==Form.id, Pokemon.id==Form.pokemon_id)'

"""Automatically generates to_dict methods for each model.

Fields in __defaultfields__ are included.
Fields in __hiddenfields__ will be ignored.

Note:
    EXTRA_FIELDS is defined for convenience in most cases. It can be passed to
    the to_dict method to produce a more verbose dictionary.
    >>> bulbasaur.to_dict(show=Pokemon.EXTRA_FIELDS)

    Alternatively, fields can be manually specified as a list.
    >>> bulbasaur.to_dict(show=['image', 'base_stats'])
"""
_BaseModel = create_base_model(db)


class Pokemon(_BaseModel):
    __tablename__ = 'pokemon'

    __defaultfields__ = [
        'evolution_chain_id', 'since_gen', 'first_type', 'second_type', 'name',
        'identifier', 'color', 'sprite', 'default_form', 'has_alt_form'
        ]

    EXTRA_FIELDS = ['image', 'flavor_text', 'forms', 'base_stats']

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    evolution_chain_id = db.Column(db.Integer)
    evolves_from_pokemon_id = db.Column(db.Integer)
    since_gen = db.Column(db.Integer, nullable=False)
    first_type_id = db.Column(db.Integer, fkey('type.id'), nullable=False)
    second_type_id = db.Column(db.Integer, fkey('type.id'))
    name = db.Column(db.String(15), unique=True, nullable=False)
    genus = db.Column(db.String(25), nullable=False)
    identifier = db.Column(db.String(12), unique=True, nullable=False)
    color = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(125), nullable=False)
    sprite = db.Column(db.String(85), nullable=False)
    flavor_text = db.Column(db.String(250))
    has_alt_form = db.Column(db.Boolean, nullable=False)

    # Computed
    forms = rel('Form', backref='pokemon', lazy=True)
    first_type = rel('Type', foreign_keys=first_type_id)
    second_type = rel('Type', foreign_keys=second_type_id)

    default_form = rel(
        'Form',
        primaryjoin=JOIN_POKE_FORM,
        uselist=False,
        lazy=True)

    @property
    def base_stats(self):
        return self.default_form.base_stats

    def __repr__(self):
        return '{name} ({id})'.format(
            name=self.name,
            id=self.id)


class Type(_BaseModel):
    """Describes a type and how it interacts with other types.

    Note:
        The relative_advantage has a specific calculation.
        Assuming the dark type.
        1. Sum all vs_* fields for the dark type.
        2. Substract the vs_dark field for every type.
        3. Divide the result by 18 (the number of types).

    Note:
        The stat_average column is calculated by averaging the stat total for
        every Pokémon which has a type in at least one of its slots.
        For example, this means that Torterra would be included in the
        calculation for both grass and ground types.
    """

    __tablename__ = 'type'

    __defaultfields__ = ['damage_class', 'identifier']

    EXTRA_FIELDS = [
        'vs_normal', 'vs_fighting', 'vs_flying', 'vs_poison', 'vs_ground',
        'vs_rock', 'vs_bug', 'vs_ghost', 'vs_steel', 'vs_fire', 'vs_water',
        'vs_grass', 'vs_electric', 'vs_psychic', 'vs_ice', 'vs_dragon',
        'vs_dark', 'vs_fairy', 'pokemon_count', 'stat_average',
        'relative_advantage', 'desc_info', 'desc_atk', 'desc_def']

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    damage_class = db.Column(db.String(10), nullable=False)
    identifier = db.Column(db.String(10), unique=True, nullable=False)
    vs_normal = db.Column(db.Float, nullable=False)
    vs_fighting = db.Column(db.Float, nullable=False)
    vs_flying = db.Column(db.Float, nullable=False)
    vs_poison = db.Column(db.Float, nullable=False)
    vs_ground = db.Column(db.Float, nullable=False)
    vs_rock = db.Column(db.Float, nullable=False)
    vs_bug = db.Column(db.Float, nullable=False)
    vs_ghost = db.Column(db.Float, nullable=False)
    vs_steel = db.Column(db.Float, nullable=False)
    vs_fire = db.Column(db.Float, nullable=False)
    vs_water = db.Column(db.Float, nullable=False)
    vs_grass = db.Column(db.Float, nullable=False)
    vs_electric = db.Column(db.Float, nullable=False)
    vs_psychic = db.Column(db.Float, nullable=False)
    vs_ice = db.Column(db.Float, nullable=False)
    vs_dragon = db.Column(db.Float, nullable=False)
    vs_dark = db.Column(db.Float, nullable=False)
    vs_fairy = db.Column(db.Float, nullable=False)
    pokemon_count = db.Column(db.Integer, nullable=False)
    stat_average = db.Column(db.Integer, nullable=False)
    relative_advantage = db.Column(db.Float, nullable=False)
    desc_info = db.Column(db.String(550), nullable=False)
    desc_atk = db.Column(db.String(850), nullable=False)
    desc_def = db.Column(db.String(850), nullable=False)

    def __repr__(self):
        return self.identifier.capitalize()


class Evolution(_BaseModel):
    """Describes how one pokemon evolves to another.

    Note:
        An evolution always has a trigger. With the exception of the trigger
        item column, every other nullable column may be present as an
        auxilliary condition for the evolution.
    """

    __tablename__ = 'evolution'

    __defaultfields__ = [
        'evolves_from', 'pokemon', 'evolution_chain_id'
        ]

    EXTRA_FIELDS = [
        'difficulty', 'trigger', 'level', 'happiness', 'trigger_item',
        'relative_stats', 'held_item', 'time_of_day', 'known_move',
        'party_pokemon', 'beauty', 'gender', 'location', 'trade_pokemon',
        'needs_inversion', 'party_type', 'needs_rain', 'known_move_type',
        'affection'
        ]

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    evolves_from_pokemon_id = db.Column(
        db.Integer, fkey('pokemon.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, fkey('pokemon.id'), nullable=False)
    evolution_chain_id = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.Float, nullable=False)
    trigger = db.Column(db.String(10), nullable=False)
    level = db.Column(db.Integer)
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

    # Computed
    evolves_from = rel('Pokemon', foreign_keys=evolves_from_pokemon_id)
    pokemon = rel('Pokemon', foreign_keys=pokemon_id)
    party_pokemon = rel('Pokemon', foreign_keys=party_pokemon_id, lazy=True)
    trade_pokemon = rel('Pokemon', foreign_keys=trade_pokemon_id, lazy=True)
    party_type = rel('Type', foreign_keys=party_type_id, lazy=True)
    known_move_type = rel('Type', foreign_keys=known_move_type_id, lazy=True)


class Form(_BaseModel):
    """Describes a specific form of a Pokémon.

    Note:
        Imagine a Coca-Cola can.
        It could be basic, it could be a diet coke, it might be a name can...

        A variant differentiates a name can from the basic can.
        The stats (nutrition info & ingredients) are the same.
        However, the labels on each can look different.
        Think: "Purely cosmetic changes."

        A different variant for the same pokemon_id is Coca-Cola vs. Diet Coke.
        The stats are different, and the looks are different.
        Even so, most people would agree that they are both still Coke.
        Think: "Functionally different Pokémon."
    """

    __tablename__ = 'form'

    __defaultfields__ = [
        'pokemon_id', 'variant_id', 'identifier', 'first_type', 'second_type',
        'alt_sprite'
        ]

    EXTRA_FIELDS = [
        'pokemon_name', 'form_label', 'alt_image', 'base_stats'
        ]

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, fkey('pokemon.id'), nullable=False)
    variant_id = db.Column(
        db.Integer, fkey('base_stats.variant_id'), nullable=False)
    pokemon_name = db.Column(db.String(25))
    first_type_id = db.Column(db.Integer, fkey('type.id'))
    second_type_id = db.Column(db.Integer, fkey('type.id'))
    identifier = db.Column(db.String(20))
    form_label = db.Column(db.String(25))
    alt_image = db.Column(db.String(130))
    alt_sprite = db.Column(db.String(100))

    # Computed
    base_stats = rel('BaseStats', backref='form', lazy=True)
    first_type = rel('Type', foreign_keys=first_type_id)
    second_type = rel('Type', foreign_keys=second_type_id)

    def __repr__(self):
        name = self.pokemon_name if self.pokemon_name else self.identifier
        return '\'{}/{}/{} –– {} –– {}\''.format(
            self.id, self.pokemon_id, self.variant_id, name, self.form_label)


class BaseStats(_BaseModel):
    """Provides baseline values for Pokémon stats.

    These values directly relate to a specific form's stat characteristics as
    it grows and levels up over time.
    """

    __tablename__ = 'base_stats'

    __defaultfields__ = [
        'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed'
        ]

    # Columns
    variant_id = db.Column(db.Integer, primary_key=True)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    special_attack = db.Column(db.Integer)
    special_defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)

    def __repr__(self):
        vals = [
            self.hp, self.attack, self.defense,
            self.special_attack, self.special_defense, self.speed]

        return '\'{}\''.format('/'.join(map(str, vals)))
