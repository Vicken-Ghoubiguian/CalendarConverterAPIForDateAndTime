#
from flask_restx import Namespace, Resource, reqparse, inputs
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
parser_current_date_and_time_by_timezone.add_argument('datetime_format', type=str, required=False, help='Available format code: \
                                                                                                           %a (abreviated weekday name), \
                                                                                                           %A (full weekday name), \
                                                                                                           %w (weekday as a decimal number), \
                                                                                                           %d (day of the month as a zero-padded decimal), \
                                                                                                           %-d (day of the month as a decimal number), \
                                                                                                           %b (abbreviated month name), %B (full month name), \
                                                                                                           %B (Full month name), \
                                                                                                           %m (Month as a zero-padded decimal number), \
                                                                                                           %-m (Month as a decimal number), \
                                                                                                           %y (Year without century as a zero-padded decimal number), \
                                                                                                           %-y (Year without century as a decimal number), \
                                                                                                           %Y (Year with century as a decimal number), \
                                                                                                           %z (UTC offset in the form +HHMM or -HHMM), \
                                                                                                           %Z (Time zone name), \
                                                                                                           %c (Locale’s appropriate date and time representation), \
                                                                                                           %x (locale’s appropriate date representation), \
                                                                                                           %X (locale’s appropriate time representation), \
                                                                                                           %% (a literal \'%\' character) \
                                                                                                           ...')
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
parser_current_date_and_time_by_timezone_for_conversion = parser_current_date_and_time_name_space.copy()

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