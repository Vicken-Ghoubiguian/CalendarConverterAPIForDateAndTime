#
from flask_restx import Namespace, Resource, inputs
from pycountry import currencies

#
from commonFunctions import *

#
languagesNamespace = Namespace('languages', description='Namespace to manipulate and get informations about all languages in the world...')

#
@languagesNamespace.route('')
class LanguagesList(Resource):

    #
    def get(self):

        """
        
        """

        return getJSONOfLanguages(), 200