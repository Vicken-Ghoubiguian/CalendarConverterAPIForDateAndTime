#
from flask_restx import Namespace, Resource
from flask import make_response, render_template

#
from commonFunctions import *

#
flagsNamespace = Namespace('flags', description='Namespace to ...')

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