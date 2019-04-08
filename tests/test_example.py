import json
import unittest

from unittest import TestCase
from idb import create_app


class ExampleTest(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_get_bulbasaur(self):
        response = self.client.get('/api/pokemon')
        result = json.loads(response.data)
        first_poke = result['data'][0]

        self.assertEqual(first_poke['identifier'], 'bulbasaur')


if __name__ == '__main__':
    unittest.main()
