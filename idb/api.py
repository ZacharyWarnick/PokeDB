from flask import Blueprint, request, jsonify, session
from sqlalchemy import create_engine

database = create_engine('sqlite:???????????')
app = Flask(__name__)
api = Blueprint('api', 'api', url_prefix='/api')

@api.route('/????????????', methods=['GET'])

class Pokemon:
    def get(self):
        conn = database.connect() # connect to database
        query = conn.execute("select * from Pokemon") # This line performs query and returns json result
        return {'Pokemon': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Evolutions:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Evolutions")
        return {'Evolutions': [i[0] for i in query.cursor.fetchall()]}

class Types:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Types")
        return {'Types': [i[0] for i in query.cursor.fetchall()]}

class Forms:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Forms")
        return {'Forms': [i[0] for i in query.cursor.fetchall()]}

class BaseStats:
    def get(self):
        conn = database.connect()
        query = conn.execute("select * from Base_Stats")
        return {'Base_Stats': [i[0] for i in query.cursor.fetchall()]}


if __name__ == '__main__':
     app.run()
