#
from flask_restx import Namespace, Resource, inputs
from pycountry import currencies

#
from commonFunctions import *

#
currentCurrenciesNamespace = Namespace('currencies', description='Namespace to manipulate and get informations about all currencies in the world...')

#
@currentCurrenciesNamespace.route('')
class CurrenciesList(Resource):

    #
    def get(self):

        """
        
        """

        return getJSONOfCurrencies(), 200