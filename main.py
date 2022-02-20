#
from flask import Flask, request
from flask_restx import Api, Resource, reqparse

#
app = Flask(__name__)

#
api = Api(app)

#
@api.route('/hello')
class HelloWorld(Resource):

    #
    def get(self):
        return {"Message": "Hello, world!"}, 200

#
if __name__ == '__main__':
    
    #
    app.run()
