#
from flask_restx import Namespace, Resource, inputs

#
from commonFunctions import *

#
flagsNamespace = Namespace('flags', description='Namespace to ...')

#
@flagsNamespace.route('')
class flagByCountry(Resource):

    #
    def post(self):

        """
        """

        #
        print("")