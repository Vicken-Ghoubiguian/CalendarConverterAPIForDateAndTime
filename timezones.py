#
from flask_restx import Namespace, Resource, reqparse
from datetime import datetime
from pytz import timezone, common_timezones, country_timezones
from pycountry import countries

#
def getAllTimezones():

    #
    all_timezones = []

    #
    for current_timezone in common_timezones:

        #
        all_timezones.append(current_timezone)

    #
    return all_timezones

#
def getCountryCodeOfTimezone(timezone):

    #
    timezones_list = country_timezones

    #
    timezone_index = -1

    #
    keys_from_timezones_list = list(timezones_list.keys())
    values_from_timezones_list = list(timezones_list.values())

    #
    for current_timezone_array in values_from_timezones_list:

        #
        if timezone in current_timezone_array:

            #
            timezone_index = values_from_timezones_list.index(current_timezone_array)

    #
    return keys_from_timezones_list[timezone_index]

#
currentDateTimeNamespace = Namespace('currentDateTime', description='Namespace to manipulate and get some informations about current datetime...')

#
parser_current_date_and_time_name_space = reqparse.RequestParser()
parser_current_date_and_time_name_space.add_argument('timezone', type=str, required=True, choices=getAllTimezones(), help='Select here the IANA (Internet Assigned Numbers Authority) timezone...')

#
parser_current_date_and_time_by_timezone = parser_current_date_and_time_name_space.copy()


#
@currentDateTimeNamespace.route('')
@currentDateTimeNamespace.expect(parser_current_date_and_time_by_timezone)
class CurrentDateTimeByTimezone(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

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
                    "country_name": countries.get(alpha_2=getCountryCodeOfTimezone(args["timezone"])).name,
                    "country_code": getCountryCodeOfTimezone(args["timezone"]),
                    "format": None
                }, 200

#
parser_current_date_and_time_by_timezone_in_particular_calendar = parser_current_date_and_time_name_space.copy()


#
@currentDateTimeNamespace.route('/particularCalendar')
@currentDateTimeNamespace.expect(parser_current_date_and_time_by_timezone_in_particular_calendar)
class CurrentDateTimeByTimezoneInParticularCalendar(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
@currentDateTimeNamespace.route('/infos')
class CurrentDateTimeByTimezoneInfos(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200