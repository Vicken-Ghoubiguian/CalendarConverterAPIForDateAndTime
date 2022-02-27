#
from flask_restx import Namespace, Resource, reqparse
from pytz import timezone, common_timezones, country_timezones
from pycountry import countries

#
timezonesNamespace = Namespace('timezones', description='Namespace to manipulate and get some informations about timezones...')

#
@timezonesNamespace.route('/infos')
class TimezonesInfos(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
@timezonesNamespace.route('/byCountries')
class TimezonesByCountries(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200
