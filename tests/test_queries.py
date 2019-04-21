import unittest

from unittest import TestCase
from idb import data, create_app
from data import ASCENDING, DESCENDING


class QueryTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app = create_app('testing')
        app.app_context().push()

    def _test_pokemon_sort(self, sort_key, first, last):
        """Tests if a sorted, paged query of Pokémon orders results correctly.

        Args:
            sort_key: 'id', 'name', 'gen', 'color', or 'type'
            first: Identifier for the first Pokémon in the sorted result.
            last: Identifier for the last Pokémon in the sorted result.
        """
        result_asc_first = data.query_pokemon_list(sort_key, ASCENDING, 1)
        pages = result_asc_first['page_count']

        result_asc_last = data.query_pokemon_list(sort_key, ASCENDING, pages)
        result_desc_first = data.query_pokemon_list(sort_key, DESCENDING, 1)
        result_desc_last = data.query_pokemon_list(sort_key, DESCENDING, pages)

        first_poke_asc = result_asc_first['data'][0]
        last_poke_asc = result_asc_last['data'][-1]
        first_poke_desc = result_desc_first['data'][0]
        last_poke_desc = result_desc_last['data'][-1]

        self.assertEqual(first_poke_asc['identifier'], first)
        self.assertEqual(first_poke_desc['identifier'], last)

        self.assertEqual(first_poke_asc, last_poke_desc)
        self.assertEqual(last_poke_asc, first_poke_desc)

    def _test_evolution_sort(self, sort_key, first, last):
        """Tests a sorted, paged query of evolutions orders results correctly.

        Args:
            sort_key: 'chain', 'diff', 'count', 'level', or 'base'
            first: Identifier for the first Pokémon in the sorted result.
            last: Identifier for the last Pokémon in the sorted result.
        """
        result_asc_first = data.query_evolution_list(sort_key, ASCENDING, 1)
        result_desc_first = data.query_evolution_list(sort_key, DESCENDING, 1)
        first_chain_asc = result_asc_first['data'][0]
        stages_first_asc = first_chain_asc['stages']
        first_chain_desc = result_desc_first['data'][0]
        stages_first_desc = first_chain_desc['stages']

        def poke_identifier(stage):
            return stage['pokemon']['identifier']

        self.assertEqual(len(stages_first_asc), len(first))
        for i, s in enumerate(first):
            self.assertEqual(poke_identifier(stages_first_asc[i]), first[i])

        self.assertEqual(len(stages_first_desc), len(last))
        for i, s in enumerate(last):
            self.assertEqual(poke_identifier(stages_first_desc[i]), last[i])

    def _test_type_sort(self, sort_key, first, last):
        result_asc_first = data.query_type_list(sort_key, ASCENDING, 1)
        page_count = result_asc_first['page_count']
        result_asc_last = data.query_type_list(sort_key, ASCENDING, page_count)
        result_desc_first = data.query_type_list(sort_key, DESCENDING, 1)
        result_desc_last = data.query_type_list(
            sort_key, DESCENDING, page_count)

        first_type_asc = result_asc_first['data'][0]
        last_type_asc = result_asc_last['data'][-1]
        first_type_desc = result_desc_first['data'][0]
        last_type_desc = result_desc_last['data'][-1]

        self.assertEqual(first_type_asc['identifier'], first)
        self.assertEqual(first_type_desc['identifier'], last)
        self.assertEqual(
            first_type_asc['identifier'], last_type_desc['identifier'])
        self.assertEqual(
            first_type_desc['identifier'], last_type_asc['identifier'])

    def test_pokemon_sorts(self):
        keys = ['id', 'name', 'gen', 'color', 'type']
        first = ['bulbasaur', 'abomasnow', 'abra', 'snorlax', 'pidgey']
        last = ['zeraora', 'zygarde', 'zeraora', 'zeraora', 'comfey']
        for (k, f, l) in zip(keys, first, last):
            with self.subTest(k):
                self._test_pokemon_sort(k, f, l)

    def test_pokemon(self):
        bulbasaur_by_id = data.query_pokemon(1)
        bulbasaur_by_name = data.query_pokemon('bulbasaur')

        self.assertEqual(bulbasaur_by_id['identifier'], 'bulbasaur')
        self.assertEqual(bulbasaur_by_id, bulbasaur_by_name)

        for i in range(2, 805):
            with self.subTest(i):
                poke_by_id = data.query_pokemon(i)
                poke_by_name = data.query_pokemon(poke_by_id['identifier'])
                self.assertEqual(poke_by_id, poke_by_name)

    def test_evolution_sorts(self):
        keys = ['chain', 'diff', 'count', 'level', 'base']
        first = [
            ['ivysaur', 'venusaur'],
            ['ninetales'],
            ['raticate'],
            ['pikachu', 'raichu'],
            ['ivysaur', 'venusaur']
            ]
        last = [
            ['naganadel'],
            [
                'vaporeon', 'jolteon', 'flareon', 'espeon',
                'umbreon', 'leafeon', 'glaceon', 'leafeon',
                'glaceon', 'sylveon', 'leafeon', 'glaceon'
                ],
            [
                'vaporeon', 'jolteon', 'flareon', 'espeon',
                'umbreon', 'leafeon', 'glaceon', 'leafeon',
                'glaceon', 'sylveon', 'leafeon', 'glaceon'
                ],
            ['zweilous', 'hydreigon'],
            ['naganadel']
            ]

        for (k, f, l) in zip(keys, first, last):
            with self.subTest(k):
                self._test_evolution_sort(k, f, l)

    def test_evolution(self):
        bases = ['bulbasaur', 'charmander', 'squirtle']
        for i in range(1, 4):
            chain = data.query_evolution(i)
            base = chain['stages'][0]['evolves_from']
            self.assertEqual(base['identifier'], bases[i - 1])

        eevee_chain_id = 67
        eevee_chain = data.query_evolution(eevee_chain_id)
        self.assertEqual(len(eevee_chain['stages']), 12)

        eeveelutions = set()
        for s in eevee_chain['stages']:
            eeveelutions.add(s['pokemon']['identifier'])

        self.assertEqual(len(eeveelutions), 8)

    def test_type_sorts(self):
        keys = ['id', 'name', 'count', 'stats', 'adv']
        first = ['normal', 'bug', 'ice', 'bug', 'grass']
        last = ['fairy', 'water', 'water', 'dragon', 'steel']

        for (k, f, l) in zip(keys, first, last):
            with self.subTest(k):
                self._test_type_sort(k, f, l)

    def test_type(self):
        normal = data.query_type('normal')
        normal_by_id = data.query_type(1)

        self.assertEqual(normal['identifier'], 'normal')
        self.assertEqual(normal, normal_by_id)

    def test_search_eevee(self):
        data.search('eevee')


if __name__ == '__main__':
    unittest.main()
