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
        wavingFlagURL = "https://flagcdn.com/160x120/" + getCountryAlpha2FromCountryName(args["country"]) + ".png"

        #
        #flagURL2 = "<img src='https://flagcdn.com/h20/" + getCountryAlpha2FromCountryName(args["country"]) + ".png' width='16' height='12' alt='" + args["country"] + "'>"

        #
        #flagURL2 = "<img src='https://flagcdn.com/h20/" + getCountryAlpha2FromCountryName(args["country"]) + ".png' width='16' height='12' alt='" + args["country"] + "'>"

        #
        countryName = args["country"]

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('flagByCountry.html', hw=args["country"], wavingFlagURL=wavingFlagURL, countryName=countryName), 200, headers)