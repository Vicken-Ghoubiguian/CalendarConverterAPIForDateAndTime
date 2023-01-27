#
from flask_restx import Namespace, Resource
from flask import make_response, render_template

#
from commonFunctions import *

#
import requests

#
flagsNamespace = Namespace('flags', description='Namespace to manipulate and get informations about all flags in the world...')

#
parser_flags = reqparse.RequestParser()

#
parser_flags.add_argument('country', type=str, required=True, choices=getAllCountriesForFlags(), help='Select the country whose flag and data you want...')

#
@flagsNamespace.route('')
@flagsNamespace.expect(parser_flags)
class FlagByCountry(Resource):

    #
    def get(self):

        """
        Get the flag and all related datas from a country or a chosen territory...
        """

        #
        args = parser_flags.parse_args()

        #
        countryAlpha2 = getCountryAlpha2FromCountryName(args["country"])

        #
        wavingFlagURL = "https://flagcdn.com/192x144/" + countryAlpha2 + ".png"

        #
        originalFlagURL = "https://flagcdn.com/h120/" + countryAlpha2 + ".png"

        #
        countryName = args["country"]

        #
        headers = {"Content-Type": "text/html"}

        #
        return make_response(render_template('flagByCountry.html', wavingFlagURL=wavingFlagURL, originalFlagURL=originalFlagURL, countryName=countryName, countryFlagEmoji=getFlagEmojiFromCountryName(countryName)), 200, headers)

#
parser_flags_to_download_flag = parser_flags.copy()
parser_flags_to_download_flag.add_argument('format', type=str, required=True, choices=['.png', '.webp', '.svg', '.jpeg'], help='Select the format you want...')
#parser_flags_to_download_flag.add_argument('size', type=str, required=True, choices=['', '', '', ''], help='Select the size you want...')

#
@flagsNamespace.route('/download')
@flagsNamespace.expect(parser_flags_to_download_flag)
class DownloadFlagByCountry(Resource):

    #
    def post(self):

        """
        
        """

        #
        args = parser_flags_to_download_flag.parse_args()

        #
        flagURL = "https://flagcdn.com/192x144/" + getCountryAlpha2FromCountryName(args["country"]) + args["format"]

        #
        try:

            #
            response = requests.get(flagURL)

            #
            open(getCountryAlpha2FromCountryName(args["country"]) + args["format"], "wb").write(response.content)

            #
            return {"code": 200, "message": "TODO"}, 200

        #
        except ConnectionError:

            #
            return {"code": 400, "message": "You are not connected to the Internet"}, 400

#
@flagsNamespace.route('/emoji')
@flagsNamespace.expect(parser_flags)
class EmojiFlagByCountry(Resource):

    #
    def get(self):

        """
        Get the flag as emoji from a country or a chosen territory...
        """

        #
        args = parser_flags.parse_args()

        #
        return {"country": args["country"], "flag": getFlagEmojiFromCountryName(args["country"])}, 200