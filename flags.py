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
parser_flags.add_argument('country', type=str, required=True, choices=getAllCountriesForFlags(), help='')

#
@flagsNamespace.route('')
@flagsNamespace.expect(parser_flags)
class flagByCountry(Resource):

    #
    def get(self):

        """
        """

        #
        args = parser_flags.parse_args()

        #
        print("\n\n\n\n" + getCountryAlpha2FromCountryName(args["country"]) + "\n\n\n\n")

        #
        url = "https://flagcdn.com/16x12/" + getCountryAlpha2FromCountryName(args["country"]) + ".png"
        countryName = args["country"]

        #
        #flagURL2 = "<img src='https://flagcdn.com/h20/" + getCountryAlpha2FromCountryName(args["country"]) + ".png' width='16' height='12' alt='" + args["country"] + "'>"

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('flagByCountry.html', url=url, countryName=countryName), 200, headers)