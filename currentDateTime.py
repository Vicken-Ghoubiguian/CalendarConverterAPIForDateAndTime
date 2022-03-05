#
from flask_restx import Namespace, Resource, reqparse
from datetime import datetime
from pytz import timezone

#
from commonFunctions import *

#
currentDateTimeNamespace = Namespace('currentDateTime', description='Namespace to manipulate and get some informations about dates and times...')

#
parser_current_date_and_time_name_space = reqparse.RequestParser()
parser_current_date_and_time_name_space.add_argument('timezone', type=str, required=True, choices=getAllTimezones(), help='Select here the IANA (Internet Assigned Numbers Authority) timezone...')

#
parser_current_date_and_time_by_timezone = parser_current_date_and_time_name_space.copy()


#
@currentDateTimeNamespace.route('')
@currentDateTimeNamespace.expect(parser_current_date_and_time_by_timezone)
class CurrentDateTimeByTimezone(Resource):

    #
    def get(self):

        """ 
        Convert and return the current datetime in the wished timezone... 
        """

        #
        date_and_time_template = "%Y-%m-%d %H:%M:%S"

        #
        args = parser_current_date_and_time_by_timezone.parse_args()

        #
        now_utc = datetime.now(timezone('UTC'))

        #
        now_from_timezone = now_utc.astimezone(timezone(args["timezone"]))

        #
        return {
                    "date_and_time": now_from_timezone.strftime(date_and_time_template), 
                    "timezone": args["timezone"],
                    "country": getCountry(args["timezone"]),
                    "format": None
                }, 200


#
@currentDateTimeNamespace.route('/byCountries')
class CurrentDateTimeByCountries(Resource):

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
parser_current_date_and_time_by_timezone_in_particular_calendar = parser_current_date_and_time_name_space.copy()


#
@currentDateTimeNamespace.route('/particularCalendar')
@currentDateTimeNamespace.expect(parser_current_date_and_time_by_timezone_in_particular_calendar)
class CurrentDateTimeByTimezoneInParticularCalendar(Resource):

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
@currentDateTimeNamespace.route('/infos')
class CurrentDateTimeByTimezoneInfos(Resource):

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200