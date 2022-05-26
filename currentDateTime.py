#
from flask_restx import Namespace, Resource, inputs
from datetime import datetime
from pytz import timezone

#
from commonFunctions import *

#
currentDateTimeNamespace = Namespace('currentDateTime', description='Namespace to manipulate and get some informations about dates and times...')

#
parser_current_date_and_time_by_timezone = parser_current_date_and_time_by_timezone_template.copy()
parser_current_date_and_time_by_timezone.add_argument('all_cdn', type=inputs.boolean, required=False, default=False, help='Do you want to include all country flags cdn\'s ?')

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
        args = parser_current_date_and_time_by_timezone.parse_args()

        #
        now_utc = datetime.now(timezone('UTC'))

        #
        now_from_timezone = now_utc.astimezone(timezone(args["timezone"]))

        #
        date_time_template = args["datetime_format"]

        #
        country = getCountry(args["timezone"], args["all_cdn"])

        #
        return {
                    "date_and_time": now_from_timezone.strftime(date_time_template) if date_time_template is not None else now_from_timezone.timestamp(),
                    "format": date_time_template if date_time_template is not None else "UTC timestamp",
                    "timezone": {
                        "name": args["timezone"],
                        "UTC offset": now_from_timezone.astimezone(timezone(args["timezone"])).strftime("%z")
                    },
                    "country": country
                }, 200


#
parser_current_date_and_time_by_timezone_for_conversion = parser_current_date_and_time_by_timezone_template.copy()

parser_current_date_and_time_by_timezone_for_conversion.add_argument('all_cdn', type=inputs.boolean, required=False, default=False, help='Do you want to include all country flags cdn\'s ?')
parser_current_date_and_time_by_timezone_for_conversion.add_argument('datetime', type=inputs.datetime_from_iso8601, default=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), required=True, help='Wished date and time in the iso8601 format according to the UTC time zone')

#
@currentDateTimeNamespace.route('/conversion')
@currentDateTimeNamespace.expect(parser_current_date_and_time_by_timezone_for_conversion)
class CurrentDateTimeConversion(Resource):

    #
    def get(self):

        """
        Convert and return the wished datetime specified in one particular format in the wished timezone...
        """

        #
        args = parser_current_date_and_time_by_timezone_for_conversion.parse_args()

        #


        #
        now_from_timezone = args["datetime"].astimezone(timezone(args["timezone"]))

        #
        country = getCountry(args["timezone"], args["all_cdn"])

        #
        return {
                    "date_and_time": str(now_from_timezone),
                    "timezone": {
                        "name": args["timezone"],
                        "UTC offset": now_from_timezone.astimezone(timezone(args["timezone"])).strftime("%z")
                    },
                    "country": country
               }, 200

#
parser_current_date_and_time_by_timezone_in_particular_calendar = parser_current_date_and_time_by_timezone_template.copy()
parser_current_date_and_time_by_timezone_in_particular_calendar.add_argument('datetime', type=inputs.datetime_from_iso8601, default=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), required=True, help='Wished date and time in the iso8601 format according to the UTC time zone')

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