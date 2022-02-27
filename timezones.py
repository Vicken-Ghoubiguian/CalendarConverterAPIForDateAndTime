#
from flask_restx import Namespace, Resource, reqparse
from pytz import timezone, common_timezones, country_timezones
from pycountry import countries

#
currentTimezonesNamespace = Namespace('timezones', description='Namespace to manipulate and get some informations about timezones...')

#
@currentTimezonesNamespace.route('/infos')
class CurrentTimezonesInfos(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200

#
@currentTimezonesNamespace.route('/byCountries')
class CurrentTimezonesByCountries(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200
