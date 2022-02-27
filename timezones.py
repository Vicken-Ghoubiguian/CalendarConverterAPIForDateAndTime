#
from flask_restx import Namespace, Resource, reqparse
from pytz import timezone, common_timezones, country_timezones
from pycountry import countries

#
currentTimezonesNamespace = Namespace('timezonesNameSpace', description='TODO...')

#
@currentTimezonesNamespace.route('/byCountries')
class CurrentTimezonesByCountries(Resource):

    #@currentDateTimeNamespace.doc('list_cats')

    #
    def get(self):

        #
        return {"TODO": "TODO"}, 200