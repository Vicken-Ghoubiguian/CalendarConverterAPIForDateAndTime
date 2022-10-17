#
from flask_restx import Namespace, Resource, inputs
from flask import make_response, render_template

#
from commonFunctions import *

#
introductionNamespace = Namespace('introduction', description='Namespace to introduce, present, explain all functionalities of the DateTime API and how it works...')

#
@introductionNamespace.route('/presentation')
class Presentation(Resource):

    #
    def get(self):

        """
        Get a presentation of the DateTime API...
        """

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('index.html'), 200, headers)