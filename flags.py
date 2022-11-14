#
from flask_restx import Namespace, Resource
from flask import make_response, render_template

#
from commonFunctions import *

#
flagsNamespace = Namespace('flags', description='Namespace to ...')

#
parser_flags = reqparse.RequestParser()

#
#parser_flags.add_argument('order', type=str, required=True, choices=["desc", "asc"], help='')

#
@flagsNamespace.route('')
class flagByCountry(Resource):

    #
    def get(self):

        """
        """

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('flagByCountry.html', hw="Hello world !"), 200, headers)