#
from flask_restx import Namespace, Resource, inputs
from flask import make_response, render_template, redirect

#
from commonFunctions import *

#
introductionNamespace = Namespace('introduction', description='Namespace to introduce, present, explain all functionalities of the DateTime API and how it works...')

#
@introductionNamespace.route('')
class Presentation(Resource):

    #
    def get(self):

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('introduction.html'), 200, headers)

#
@introductionNamespace.route('/presentation')
class Presentation(Resource):

    #
    def get(self):

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('presentation.html'), 200, headers)

#
@introductionNamespace.route('/history')
class History(Resource):

    #
    def get(self):

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('history.html'), 200, headers)

#
@introductionNamespace.route('/github')
class GitHub(Resource):

    #
    def get(self):

        """
        Redirect to the DateTime API's GitHub repository...
        """

        #
        return redirect("https://github.com/Vicken-Ghoubiguian/DateTimeAPI", code=302)

#
@introductionNamespace.route('/dockerhub')
class DockerHub(Resource):

    #
    def get(self):

        """
        
        """

        #
        return redirect("https://www.google.com", code=302)