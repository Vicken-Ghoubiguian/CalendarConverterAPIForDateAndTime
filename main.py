#
from flask import Flask, url_for
from flask_restx import Api
from currentDateTime import currentDateTimeNamespace as nsdt
from timezones import timezonesNamespace as nstz
#from calendar import CalendarNamespace as cc
from truc import truc as tr

#
app = Flask(__name__)

api = Api(
    title='MathematicalDateTimeAPI',
    version='1.0',
    description='...'
)

#
api.add_namespace(nsdt)
api.add_namespace(nstz)
#api.add_namespace(cc)
api.add_namespace(tr)

#
api.init_app(app)

#
if __name__ == '__main__':
    
    #
    app.run()