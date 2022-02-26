#
from asyncio.windows_events import NULL
from tokenize import String
from flask import Flask, request
from flask_restx import Api, Resource, reqparse
from datetime import datetime
from pytz import timezone

#
app = Flask(__name__)

#
api = Api(app)

#
parser_current_date_and_time_by_timezone = reqparse.RequestParser()
parser_current_date_and_time_by_timezone.add_argument('timezone', type=str, required=True, help='Enter here the IANA (Internet Assigned Numbers Authority) timezone...')

#
@api.route('/currentDateTime')
@api.expect(parser_current_date_and_time_by_timezone)
class CurrentDateTimeByTimezone(Resource):

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
@api.route('/currentDate/particularCalendar')
class CurrentDateTimeByTimezoneInParticularCalendar(Resource):

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
if __name__ == '__main__':
    
    #
    app.run()
