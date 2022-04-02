#
from flask_restx import Namespace, Resource, reqparse, inputs
from pytz import timezone, common_timezones, country_timezones

#
from commonFunctions import *

#
timezonesNamespace = Namespace('timezones', description='Namespace to manipulate and get some informations about timezones...')

#
parser_timezones_infos = reqparse.RequestParser()
parser_timezones_infos.add_argument('timezone', type=str, required=True, choices=getAllTimezones(), help='Select here the IANA (Internet Assigned Numbers Authority) timezone...')
parser_timezones_infos.add_argument('all_cdn', type=inputs.boolean, required=False, default=False, help='Do you want to include all country flags cdn\'s ?')

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
        now_utc = datetime.now(timezone('UTC'))

        #
        country = getCountry(args["timezone"], bool(args["all_cdn"]))

        #
        return {
                    "timezone": {
                        "name": args["timezone"],
                        "UTC offset": now_utc.astimezone(timezone(args["timezone"])).strftime("%z")
                    },
                    "country": country,
                }, 200

#
parser_timezones_by_country = reqparse.RequestParser()

#
parser_timezones_by_country.add_argument('country', type=str, required=True, choices=getAllCountries(), help='Select here the country...')
parser_timezones_by_country.add_argument('all_cdn', type=inputs.boolean, required=False, default=False, help='Do you want to include all country flags cdn\'s ?')
parser_timezones_by_country.add_argument('all_infos', type=inputs.boolean, required=False, default=False, help='Do you want all informations about timezones\'s ?')

#
@timezonesNamespace.route('/byCountry')
@timezonesNamespace.expect(parser_timezones_by_country)
class TimezonesByCountries(Resource):

    #
    def get(self):

        """
        Get all timezones (with all informations) for a selected country...
        """

        #
        args = parser_timezones_by_country.parse_args()

        #
        all_timezones_by_country = getAllTimezonesByCountry(args["country"], args["all_infos"])

        #
        if args["all_infos"]:

            #
            return {"TODO": "TODO"}, 200

        #
        else:

            #
            country = getCountry(all_timezones_by_country[0], args["all_cdn"])

            #
            return {
                    "country": country,
                    "timezones": all_timezones_by_country
                }, 200
