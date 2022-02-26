#
from flask import Flask, request
from flask_restx import Api
from timezones import currentDateNamespace as nstz

#
app = Flask(__name__)

api = Api(
    title='CalendarConverterAPIForDateAndTime',
    version='1.0',
    description='A converter API for date and time in many calendars in the world (Gregorian, Julian, Chinese, Solar Hijri, Maya, Republican...)...'
)

#
api.add_namespace(nstz)

#
api.init_app(app)

#
if __name__ == '__main__':
    
    #
    app.run()
