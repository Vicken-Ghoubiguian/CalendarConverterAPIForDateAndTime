#
from flask_restx import Namespace, Resource, reqparse
from pytz import timezone, common_timezones, country_timezones

#
from commonFunctions import *

#
timezonesNamespace = Namespace('timezones', description='Namespace to manipulate and get some informations about timezones...')

#
parser_timezones_infos = reqparse.RequestParser()
parser_timezones_infos.add_argument('timezone', type=str, required=True, choices=getAllTimezones(), help='Select here the IANA (Internet Assigned Numbers Authority) timezone...')

#
@timezonesNamespace.route('')
@timezonesNamespace.expect(parser_timezones_infos)
class TimezonesInfos(Resource):

    #
    def get(self):

        """
        Get all informations about the wished timezone...
        """

        #
        args = parser_timezones_infos.parse_args()

        #
        country = getCountry(args["timezone"])

        #
        now_utc = datetime.now(timezone('UTC'))

        #
        country = getCountry(args["timezone"])

        #
        return {
                    "timezone": args["timezone"],
                    "UTC offset": now_utc.astimezone(timezone(args["timezone"])).strftime("%z"),
                    "country": country,
                }, 200

#
parser_timezones_by_country = reqparse.RequestParser()

#
parser_timezones_by_country.add_argument('country', type=str, required=True, choices=getAllCountries(), help='Select here the country...')

#
@timezonesNamespace.route('/byCountry')
@timezonesNamespace.expect(parser_timezones_by_country)
class TimezonesByCountries(Resource):

    #
    def get(self):

        """
        Get all timezones (with informations) for a selected country...
        """

        #
        args = parser_timezones_by_country.parse_args()

        #


        #
        return {
                    "TODO": "TODO"
                }, 200
