#
from flask_restx import Namespace, Resource, inputs
from pycountry import countries

#
from commonFunctions import *

#
currentCountriesNamespace = Namespace('countries', description='Namespace to manipulate and get informations about all countries in the world...')

#
@currentCountriesNamespace.route('/list')
class CountriesList(Resource):

    #
    def get(self):

        """
        
        """

        #
        return {"TODO": "TODO"}, 200