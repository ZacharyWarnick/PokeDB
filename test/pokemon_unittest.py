#import os
import unittest import main, TestCase

import sys
sys.path.append("../")

from flask import request, json, jsonify, session, Blueprint
from idb import api, app, db, data

app = Flask(__name__)
app.register_blueprint(api)
    # “””Test case for the client methods.”””
    def setup(self):
        


class ApiTests(unittest.TestCase):
    
    def setUp(self):
        app.app.config["TESTING"] = True
        self.app = app.app.test_client()
    
    
    
    
    
        # Test of pokemon get function function
        
        def test_get_pokemon1(self):
            with app.test_request_context():
                # mock object
                
                target = "bulbasaur"
                out = self.app.get('api/pokemon/bulbasaur')
                first_poke = json.loads(out.data['identifier'](as_text=True))
            
            
            
            # Passing the mock object
            response = [
                        {
                        "name": "Bulbasaur",
                        "genus": "Seed Pokémon",
                        "identifier": "bulbasaur",
                        "evolution_chain": 1,
                        "color": "green",
                        "since_gen": 1,
                        "evolves_from": null,
                        "type1": 12,
                        "type2": 4,
                        "flavor_text": "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun’s rays,\nthe seed grows progressively larger.",
                        "has_alt_form": false,
                        "id": 1,
                        "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
                        "image": "https://archives.bulbagarden.net/media/upload/thumb/2/21/001Bulbasaur.png/600px-001Bulbasaur.png"
                        
                        }
                        ]
                
                    self.assertEqual(out, response)
                
            def test_get_pokemon2(self):
                with app.test_request_context():
            # mock object
            
            
            
            target = "Krookodile"
            out = self.app.get('api/pokemon/krookodile')
            first_poke = json.loads(out.data['identifier'](as_text=True))
                        # Passing the mock object
            response = [
                        {
                        "name": "Krookodile",
                        "genus": "Intimidation Pokémon",
                        "identifier": "krookodile",
                        "evolution_chain": 281,
                        "color": "red",
                        "since_gen": 5,
                        "evolves_from": 552,
                        "type1": 5,
                        "type2": 17,
                        "flavor_text": "When it spots prey, even at a distance of over\n30 miles, it swims through the desert as if it\nwere water, then jumps out and chomps them.",
                        "has_alt_form": false,
                        "id": 553,
                        "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/553.png",
                        "image": "https://archives.bulbagarden.net/media/upload/thumb/e/e5/553Krookodile.png/600px-553Krookodile.png"
                        
                        }
                        ]
                
            self.assertEqual(out, response)
            
            def test_get_pokemon3(self):
                with app.test_request_context():
                    target = "Bruxish"
                        # mock object
                out = self.app.get('api/pokemon/bruxish')
                first_poke = json.loads(out.data['identifier'](as_text=True))
                            # Passing the mock object
                response = [
                            {
                            "name": "Bruxish",
                            "genus": "Gnash Teeth Pokémon",
                            "identifier": "bruxish",
                            "evolution_chain": null,
                            "color": "pink",
                            "since_gen": 7,
                            "evolves_from": null,
                            "type1": 11,
                            "type2": 14,
                            "flavor_text": "It burrows beneath the sand, radiating\npsychic power from the protuberance on its\nhead. It waits for prey as it surveys the area.",
                            "has_alt_form": false,
                            "id": 779,
                            "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/779.png",
                            "image": "https://archives.bulbagarden.net/media/upload/thumb/9/92/779Bruxish.png/600px-779Bruxish.png"
                            
                            }
                            ]
                # data = json.loads(out.get_data(as_text=True))
                # Assert response
                self.assertEqual(out, response)

                        
                        
                        #double check what get returns
        def test_api_evolutions_1(self):
            with app.test_request_context():
                # mock object
                out = self.app.get('evolutions/ekans')
    #            first_poke = json.loads(out.data['identifier'](as_text=True))
                # Passing the mock object
                response = [
                            {
                            "evolves_from": 1,
                            "result": 2,
                            "chain": 1,
                            "trigger": "level-up",
                            "level": 16,
                            "id": 1,
                            "difficulty": 0.46
                            
                            }
                            ]
                data = json.loads(out.data(as_text=True))
                            # Assert response
                self.assertEqual(data, response)
        
        def test_api_evolutions_2(self):
            with app.test_request_context():
                # mock object
                out = self.app.get('evolutions/sandshrew')
            # Passing the mock object
            response = [
                        {
                        "evolves_from": 444,
                        "result": 445,
                        "chain": 230,
                        "trigger": "level-up",
                        "level": 48,
                        "id": 222,
                        "difficulty": 1.26
                        
                        }
                        ]
            data = json.loads(out.data(as_text=True))
                        # Assert response
            self.assertEqual(data, response)

        def test_api_evolutions_3(self):
            with app.test_request_context():
                # mock object
                out = self.app.get('evolutions/magikarp')
                # Passing the mock object
            response = [
                        {
                        "evolves_from": 729,
                        "result": 730,
                        "chain": 376,
                        "trigger": "level-up",
                        "level": 34,
                        "id": 378,
                        "difficulty": 0.91
                        
                        }
                        ]
            data = json.loads(out.data(as_text=True))
                            # Assert response
            self.assertEqual(data, response)
    
    
    
    
    
#    def test_api_forms_1(self):
#        with app.test_request_context():
#            # mock object
#            out = api.Forms.get()
#        # Passing the mock object
#        response = [
#                    {
#                    "identifier": "normal",
#                    "pokemon_id": 386,
#                    "pokemon_variant": 386,
#                    "pokemon_name": "Normal Deoxys",
#                    "form_label": "Normal Forme",
#                    "type1": 14,
#                    "type2": null,
#                    "id": 386
#
#                    }
#                    ]
#                    data = json.loads(out.get_data(as_text=True))
#                    # Assert response
#                self.assertEqual(data['1'], response)
#
#def test_api_forms_2(self):
#    with app.test_request_context():
#        # mock object
#        out = api.Forms.get()
#        # Passing the mock object
#        response = [
#                    {
#                    "identifier": "incarnate",
#                    "pokemon_id": 642,
#                    "pokemon_variant": 642,
#                    "pokemon_name": "Incarnate Thundurus",
#                    "form_label": "Incarnate Forme",
#                    "type1": 13,
#                    "type2": 3,
#                    "id": 642
#
#                    }
#                    ]
#                    data = json.loads(out.get_data(as_text=True))
#                    # Assert response
#        self.assertEqual(data['16'], response)
#
#    def test_api_forms_3(self):
#        with app.test_request_context():
#            # mock object
#            out = api.Forms.get()
#        # Passing the mock object
#        response = [
#                    {
#                    "identifier": "aria",
#                    "pokemon_id": 648,
#                    "pokemon_variant": 648,
#                    "pokemon_name": "Aria Meloetta",
#                    "form_label": "Aria Forme",
#                    "type1": 1,
#                    "type2": 14,
#                    "id": 648
#
#                    }
#                    ]
#                    data = json.loads(out.get_data(as_text=True))
#                    # Assert response
#                self.assertEqual(data['19'], response)
#
#def test_api_base_stats_1(self):
#    with app.test_request_context():
#        # mock object
#        out = api.Base_Stats.get()
#        # Passing the mock object
#        response = [
#                    {
#                    "hp": 45,
#                    "attack": 49,
#                    "defense": 49,
#                    "special-attack": 65,
#                    "special-defense": 65,
#                    "speed": 45,
#                    "id": 1
#
#                    }
#                    ]
#                    data = json.loads(out.get_data(as_text=True))
#                    # Assert response
#        self.assertEqual(data['0'], response)
#
#    def test_api_base_stats_2(self):
#        with app.test_request_context():
#            # mock object
#            out = api.Base_Stats.get()
#        # Passing the mock object
#        response = [
#                    {
#                    "hp": 50,
#                    "attack": 50,
#                    "defense": 40,
#                    "special-attack": 50,
#                    "special-defense": 40,
#                    "speed": 64,
#                    "id": 535
#
#                    }
#                    ]
#                    data = json.loads(out.get_data(as_text=True))
#                    # Assert response
#                self.assertEqual(data['534'], response)
#
#def test_api_base_stats_3(self):
#    with app.test_request_context():
#        # mock object
#        out = api.Base_Stats.get()
#        # Passing the mock object
#        response = [
#                    {
#                    "hp": 79,
#                    "attack": 103,
#                    "defense": 120,
#                    "special-attack": 135,
#                    "special-defense": 115,
#                    "speed": 78,
#                    "id": 10036
#
#                    }
#                    ]
#                    data = json.loads(out.get_data(as_text=True))
#                    # Assert response
#        self.assertEqual(data['10035'], response)

        def test_api_Types_1(self):
            with app.test_request_context():
                # mock object
            out = self.app.get('types/normal')
            # Passing the mock object
            response = [
                        {
                        "damage_class": "physical",
                        "identifier": "normal",
                        "vs_normal": 1.0,
                        "vs_fighting": 1.0,
                        "vs_flying": 1.0,
                        "vs_poison": 1.0,
                        "vs_ground": 1.0,
                        "vs_rock": 0.5,
                        "vs_bug": 1.0,
                        "vs_ghost": 0.0,
                        "vs_steel": 0.5,
                        "vs_fire": 1.0,
                        "vs_water": 1.0,
                        "vs_grass": 1.0,
                        "vs_electric": 1.0,
                        "vs_psychic": 1.0,
                        "vs_ice": 1.0,
                        "vs_dragon": 1.0,
                        "vs_dark": 1.0,
                        "vs_fairy": 1.0,
                        "id": 1,
                        "pokemon_count": 109,
                        "stat_average": 398,
                        "relative_advantage": -0.111,
                        "desc_info": "The Normal type is the most basic type of Pokémon. They are very common and appear from the very first route you visit. Most Normal Pokémon are single type, but there is a large contingent having a second type of Flying. Pokémon X/Y add several Normal dual-type Pokémon.",
                        "desc_atk": "The Normal type is the only type that is not super effective against any other type. \n\nThe combination of Normal and Ground-type moves provides good neutral coverage, with only five type combinations resisting both, because Ground covers both of the types that resist Normal. Their inability to hit Ghost-type Pokémon can be nullified by using Foresight, Odor Sleuth, or by Pokémon with the Ability Scrappy. In these cases, it will provide unresisted coverage when paired with Fighting-type moves (excluding Pokémon with Wonder Guard). \n\nOn average, fully evolved Pokémon with the Normal type have the lowest base Special Attack of all types. \n",
                        "desc_def": "The Normal type is tied with the Electric type for the fewest defensive weaknesses, but with no resistances and one immunity, it is also tied with Ice as the least resistant type. Many Normal-type Pokémon with a secondary type mitigate their weakness with the secondary type (as with Flying, the type most commonly paired with Normal), leaving them with only the weaknesses of their secondary type. \n\nNormal-type Pokémon, on average, have the lowest Defense and Special Defense of all Pokémon and of fully evolved Pokémon.\n"
                        
                        }
                        ]
                data = json.loads(out.data(as_text=True))
                        # Assert response
                self.assertEqual(data, response)

        def test_api_Types_2(self):
            with app.test_request_context():
                # mock object
                out = self.app.get('types/fire')
                # Passing the mock object
            response = [
                        {
                        "damage_class": "special",
                        "identifier": "fire",
                        "vs_normal": 1.0,
                        "vs_fighting": 1.0,
                        "vs_flying": 1.0,
                        "vs_poison": 1.0,
                        "vs_ground": 1.0,
                        "vs_rock": 0.5,
                        "vs_bug": 2.0,
                        "vs_ghost": 1.0,
                        "vs_steel": 2.0,
                        "vs_fire": 0.5,
                        "vs_water": 0.5,
                        "vs_grass": 2.0,
                        "vs_electric": 1.0,
                        "vs_psychic": 1.0,
                        "vs_ice": 2.0,
                        "vs_dragon": 0.5,
                        "vs_dark": 1.0,
                        "vs_fairy": 1.0,
                        "id": 10,
                        "pokemon_count": 64,
                        "stat_average": 447,
                        "relative_advantage": 0.111,
                        "desc_info": "Fire is one of the three basic elemental types along with Water and Grass, which constitute the three starter Pokémon. This creates a simple triangle to explain the type concept easily to new players. Fire types are notoriously rare in the early stages of the games so choosing the Fire variation starter is often a plus.",
                        "desc_atk": "During harsh sunlight or extremely harsh sunlight, the power of Fire-type attacks is increased by 50%. The power of Fire-type attacks is decreased by 50% during rain, while all Fire-type moves will fail during heavy rain. When Water Sport is in the effect, the power of Fire-type moves are decreased by 50%. When used under the effect of Powder, Fire attacks will damage the user by 1/4 of its max HP instead of executing normally.\n\nBecause Fire is super effective against Grass and Bug, it combines well with Ground-type attacks. \n",
                        "desc_def": "Very few Fire-type Pokémon have a secondary type that negates their weakness to Water-type attacks. On the other hand, most Fire types can learn Solar Beam to counter all three of the type's weaknesses. \n\nThe Fire type grants immunity to burns and the sea of fire caused by Grass Pledge and Fire Pledge. It enables the use of Burn Up, though Burn Up removes the user's Fire type.\n"
                        
                        }
                        ]
                data = json.loads(out.data(as_text=True))
                            # Assert response
                self.assertEqual(data, response)
        
        def test_api_Types_3(self):
            with app.test_request_context():
                # mock object
                out = self.app.get('types/fairy')
            # Passing the mock object
            response = [
                        {
                        "damage_class": "special",
                        "identifier": "fairy",
                        "vs_normal": 1.0,
                        "vs_fighting": 2.0,
                        "vs_flying": 1.0,
                        "vs_poison": 0.5,
                        "vs_ground": 1.0,
                        "vs_rock": 1.0,
                        "vs_bug": 1.0,
                        "vs_ghost": 1.0,
                        "vs_steel": 0.5,
                        "vs_fire": 0.5,
                        "vs_water": 1.0,
                        "vs_grass": 1.0,
                        "vs_electric": 1.0,
                        "vs_psychic": 1.0,
                        "vs_ice": 1.0,
                        "vs_dragon": 2.0,
                        "vs_dark": 2.0,
                        "vs_fairy": 1.0,
                        "id": 18,
                        "pokemon_count": 47,
                        "stat_average": 416,
                        "relative_advantage": 0.111,
                        "desc_info": "The Fairy type was introduced in Generation 6 - the first new type for more than 12 years! Its main intention was to balance the type chart by reducing the power of dragons, while also giving an offensive boost to the Poison and Steel types. Several old Pokémon were retyped and new Pokémon introduced. In total there are just 34 Fairy type Pokémon (not including Megas/Formes), slightly above Ice.",
                        "desc_atk": "Fairy attacks are resisted by Poison, but Poison is weak to Psychic-type moves, which Fairy Pokémon are frequently able to learn. Additionally, all three of the types that resist Fairy are weak to Ground, making Fairy and Ground a strong attacking combination. \n\nFairy-type Pokémon, on average, have the lowest physical Attack of all Pokémon. \n",
                        "desc_def": "The Pokémon of this type have the highest average Special Defense of all types. \n"
                        
                        }
                        ]
                data = json.loads(out.data(as_text=True))
                        # Assert response
                self.assertEqual(data, response)


#class TestFunctions(TestCase):




if __name__ == "__main__":
    unittest.main()
