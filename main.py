#
from flask import Flask, url_for
from flask_restx import Api
from currentDateTime import currentDateTimeNamespace as nsdt
from timezones import timezonesNamespace as nstz
from calendarFromCurrentAPI import CalendarNamespace as cc
from countries import currentCountriesNamespace as ct
from introduction import introductionNamespace as nsi

#
app = Flask(__name__)

api = Api(
    title='WorldSwissKnifeAPI',
    version='1.0',
    description='Rest API which is also a swiss knife and to which you can add all the features you want, and like many others, it\'s a REST API just for experimenting and laughing 🇨🇭🔪...'
)

#
api.add_namespace(nsi)
api.add_namespace(nsdt)
api.add_namespace(nstz)
api.add_namespace(cc)
api.add_namespace(ct)

#
api.init_app(app)

#
if __name__ == '__main__':
    
    #
    app.run()
