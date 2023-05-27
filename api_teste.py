from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TesteResource(Resource):
    def get(self):
        return {'message': 'GET method called'}

    def post(self):
        data = request.get_json()
        return {'message': 'POST method called', 'data': data}

    def delete(self):
        return {'message': 'DELETE method called'}

api.add_resource(TesteResource, '/teste')

if __name__ == '__main__':
    app.run(debug=True)