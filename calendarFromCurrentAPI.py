#
from flask_restx import Namespace, Resource, reqparse, inputs
from pytz import timezone, common_timezones, country_timezones

#
from commonFunctions import *

CalendarNamespace = Namespace('calendar', description='Namespace to date and time in many calendars in the world (Gregorian, Julian, Chinese, Solar Hijri, Maya, Republican...)...')

#
@CalendarNamespace.route('/list')
class CalendarList(Resource):

    #
    def get(self):

        """
        Get all available calendars to convert dates and times...
        """

        #
        return {"available_calendars": getAllCalendars()}, 200

#
parser_particular_calendar_current_datetime = reqparse.RequestParser()
parser_particular_calendar_current_datetime.add_argument('calendar', type=str, required=True, choices=getAllCalendars(), help='Select here the calendar system you want for conversion...')

@CalendarNamespace.route('/currentDatetime')
@CalendarNamespace.expect(parser_particular_calendar_current_datetime)
class CalendarConversionParticularCalendarCurrentDatetime(Resource):

    #
    def get(self):

        """
        Get the current datetime in the wished calendar system...
        """

        #
        args = parser_particular_calendar_current_datetime.parse_args()

        #
        return {"TODO": "TODO"}, 200

@CalendarNamespace.route('/wishedDatetime')
class CalendarConversionParticularCalendarWishedDatetime(Resource):

    #
    def get(self):

        """
        Get the wished datetime in the wished calendar system...
        """

        #
        return {"TODO": "TODO"}, 200