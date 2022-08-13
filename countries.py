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
        Get the list of all existing countries in the world...
        """

        #
        return getJSONOfCountries(list(pycountry.countries)), 200

#
@currentCountriesNamespace.route('/list/historical_countries')
class HistoricalCountriesList(Resource):

    #
    def get(self):

        """
        Get the list of all existing countries in the world...
        """

        #
        return getJSONOfHistoricalCountries(list(pycountry.historic_countries)), 200