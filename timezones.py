#
from flask_restx import Namespace, Resource, reqparse
from datetime import datetime
from pytz import timezone

#
currentDateTimeNamespace = Namespace('currentDateTime', description='Namespace to manipulate and get some informations about current datetime...')

#
parser_current_date_and_time_name_space = reqparse.RequestParser()
parser_current_date_and_time_name_space.add_argument('timezone', type=str, required=True, help='Enter here the IANA (Internet Assigned Numbers Authority) timezone...')

#
parser_current_date_and_time_by_timezone = reqparse.RequestParser()
parser_current_date_and_time_by_timezone.add_argument('timezone', type=str, required=True, help='Enter here the IANA (Internet Assigned Numbers Authority) timezone...')

#
@currentDateTimeNamespace.route('')
@currentDateTimeNamespace.expect(parser_current_date_and_time_by_timezone)
class CurrentDateTimeByTimezone(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        try:

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
                    "time": now_from_timezone.strftime(date_and_time_template), 
                    "timezone": args["timezone"],
                    "lat": None,
                    "lon": None
                    }, 200

        #
        except Exception as exp:

            #
            return {"error": exp.string()}, 200

#
parser_current_date_and_time_by_timezone_in_particular_calendar = parser_current_date_and_time_by_timezone.copy()


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