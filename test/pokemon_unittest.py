#import os
import unittest

from flask import request, json, jsonify





import sys
sys.path.append('../')
from idb import app



TEST_DB = 'test.loader_path'


class BasicTests(unittest.TestCase):
    
    ############################
    #### setup and teardown ####
    ############################
    
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
#        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
#        db.drop_all()
#        db.create_all()
        
        
        assertEqual(app.debug, False)

# executed after each test
def tearDown(self):
    pass
    
    
    ###############
    #### tests ####
    ###############
    
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
#
#@app.route('/idb/data')
#def poke():
#    json_data = request.get_json()
#    email = json_data['POKEMON']
##    password = json_data['password']
#    return jsonify(email)
#
#with app.test_client() as c:
#    rv = c.post('/idb/data', json={
#                'username': 'flask', 'password': 'secret'
#                })
#                json_data = rv.get_json()
#                assert verify_token(email, json_data['token'])


if __name__ == "__main__":
    unittest.main()
