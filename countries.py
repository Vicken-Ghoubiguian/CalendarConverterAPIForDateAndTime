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
@currentCountriesNamespace.route('/list/historical')
class HistoricalCountriesList(Resource):

    #
    def get(self):

        """
        Get the list of all ancient countries in the world...
        """

        #
        return getJSONOfHistoricalCountries(list(pycountry.historic_countries)), 200

#
parser_sort_name = reqparse.RequestParser()

#
parser_sort_name.add_argument('pattern', type=str, required=True, help='Fill in the pattern you want...')
#parser_sort_name.add_argument('order', type=str, required=True, choices=["desc", "asc"], help='')

#
@currentCountriesNamespace.route('/sort/name')
@currentCountriesNamespace.expect(parser_sort_name)
class CountriesSortName(Resource):

    #
    def get(self):

        """
        Get the list of all ancient countries selected according a pattern...
        """

        #
        args = parser_sort_name.parse_args()

        #
        return getJSONofCountriesFromSort(list(pycountry.countries), field = "name", pattern = args["pattern"]), 200

#
@currentCountriesNamespace.route('/sort/alpha_2')
class CountriesSortAlpha2(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/sort/alpha_3')
class CountriesSortAlpha3(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/historical/sort/name')
class CountriesSortName(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/historical/sort/alpha_2')
class CountriesSortAlpha2(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200

#
@currentCountriesNamespace.route('/historical/sort/alpha_3')
class CountriesSortAlpha3(Resource):

    #
    def get(self):

        """
        """

        #
        return {"TODO": "TODO"}, 200