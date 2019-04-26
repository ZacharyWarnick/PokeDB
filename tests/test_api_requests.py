import json
import unittest

from unittest import TestCase
from idb import create_app
from pprint import pprint


class TestApiRequests(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def _test_get_pokemon(self, pokemon, expectations):
        out = self.client.get('/api/pokemon/{}'.format(pokemon))
        poke = json.loads(out.data)

        for key, value in expectations.items():
            if '.' in key:
                resp = poke
                for nkey in key.split('.'):
                    # Obtain the nested element.
                    resp = resp[nkey]
            else:
                resp = poke[key]

            with self.subTest('{}.{}'.format(pokemon, key)):
                self.assertEqual(value, resp)

    def _test_get_evolution(self, evo, expectations):
        out = self.client.get('/api/evolutions/{}'.format(evo))
        poke = json.loads(out.data)

        for key, value in expectations.items():
            if '.' in key:
                resp = poke
                for nkey in key.split('.'):
                    # Obtain the nested element.
                    resp = resp[nkey]
            else:
                resp = poke[key]

            for i in range(len(resp)):
                for innerkey, innervalue in value[i].items():
                    idnum = resp[i][innerkey]


                with self.subTest('{}.{}'.format(evo, key)):
                    self.assertEqual(innervalue, idnum)

    def _test_get_type(self, types, expectations):
        out = self.client.get('/api/types/{}'.format(types))
        poke = json.loads(out.data)

        for key, value in expectations.items():
            if '.' in key:
                resp = poke
                for nkey in key.split('.'):
                    # Obtain the nested element.
                    resp = resp[nkey]
            else:
                resp = poke[key]

            with self.subTest('{}.{}'.format(types, key)):
                self.assertEqual(value, resp)

    def test_get_pokemon_identifier(self):
        expectations = {
            'bulbasaur': {
                'identifier': 'bulbasaur',
                },
            'krookodile': {
                'identifier': 'krookodile',
                }
            }

        for k, v in expectations.items():
            self._test_get_pokemon(k, v)

    def test_get_pokemon_types(self):
        expectations = {
            'bulbasaur': {
                'evolution_chain_id': 1,
                'first_type.identifier': 'grass',
                'second_type.identifier': 'poison'
                }
            }

        for k, v in expectations.items():
            self._test_get_pokemon(k, v)

    def test_get_evo_wurmple(self):
        """Wurmple's evolution chain diverges at it's first evolution.

        Both possible evolutions then evolve independently.
        """
        expectations = {
            '135': {
                'stages': [{'id': 138},{'id': 139},{'id': 140},{'id': 141}]
                }
            }
        for k, v in expectations.items():
            self._test_get_evolution(k, v)
       

    def test_get_evo_eevee(self):
        """Eevee has 8 evolutions. Two can evolve in 3 different ways."""
        expectations = {
            '67': {
                'stages': [{'id': 76},{'id': 77},{'id': 78},{'id': 109},{'id': 110},{'id': 238},{'id': 239},{'id': 324},{'id': 325},{'id': 361},{'id': 363},{'id': 364}]
                }
            }
        for k, v in expectations.items():
            self._test_get_evolution(k, v)
        



    def test_get_evo_magikarp(self):
        """Has a simple, level-based evolution. This is the average case."""
        expectations = {
            '64': {
                'stages': [{'id': 75}]
                }
            }
        for k, v in expectations.items():
            self._test_get_evolution(k, v)
        

    

    def test_get_type_normal(self):
        expectations = {
            'normal': {
                'damage_class': 'physical',
                'identifier': 'normal',
                'vs_normal': 1.0,
                'vs_fighting': 1.0,
                'vs_flying': 1.0,
                'vs_poison': 1.0,
                'vs_ground': 1.0,
                'vs_rock': 0.5,
                'vs_bug': 1.0,
                'vs_ghost': 0.0,
                'vs_steel': 0.5,
                'vs_fire': 1.0,
                'vs_water': 1.0,
                'vs_grass': 1.0,
                'vs_electric': 1.0,
                'vs_psychic': 1.0,
                'vs_ice': 1.0,
                'vs_dragon': 1.0,
                'vs_dark': 1.0,
                'vs_fairy': 1.0,
                'id': 1,
                'pokemon_count': 109,
                'stat_average': 398,
                'relative_advantage': -0.111
                }
            }
        for k, v in expectations.items():
            self._test_get_type(k, v)
        

    def test_get_type_fire(self):
        expectations = {
            'fire': {
                'damage_class': 'special',
                'identifier': 'fire',
                'vs_normal': 1.0,
                'vs_fighting': 1.0,
                'vs_flying': 1.0,
                'vs_poison': 1.0,
                'vs_ground': 1.0,
                'vs_rock': 0.5,
                'vs_bug': 2.0,
                'vs_ghost': 1.0,
                'vs_steel': 2.0,
                'vs_fire': 0.5,
                'vs_water': 0.5,
                'vs_grass': 2.0,
                'vs_electric': 1.0,
                'vs_psychic': 1.0,
                'vs_ice': 2.0,
                'vs_dragon': 0.5,
                'vs_dark': 1.0,
                'vs_fairy': 1.0,
                'id': 10,
                'pokemon_count': 64,
                'stat_average': 447,
                'relative_advantage': 0.111
                }
            }
        for k, v in expectations.items():
            self._test_get_type(k, v)
        

    def test_api_type_fairy(self):
        expectations = {
            'fairy': {
                'damage_class': 'special',
                'identifier': 'fairy',
                'vs_normal': 1.0,
                'vs_fighting': 2.0,
                'vs_flying': 1.0,
                'vs_poison': 0.5,
                'vs_ground': 1.0,
                'vs_rock': 1.0,
                'vs_bug': 1.0,
                'vs_ghost': 1.0,
                'vs_steel': 0.5,
                'vs_fire': 0.5,
                'vs_water': 1.0,
                'vs_grass': 1.0,
                'vs_electric': 1.0,
                'vs_psychic': 1.0,
                'vs_ice': 1.0,
                'vs_dragon': 2.0,
                'vs_dark': 2.0,
                'vs_fairy': 1.0,
                'id': 18,
                'pokemon_count': 47,
                'stat_average': 416,
                'relative_advantage': 0.111
                }
            }
        for k, v in expectations.items():
            self._test_get_type(k, v)
        


if __name__ == '__main__':
    unittest.main()
