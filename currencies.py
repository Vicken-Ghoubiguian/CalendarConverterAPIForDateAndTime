#
from flask_restx import Namespace, Resource, inputs
from pycountry import currencies

#
from commonFunctions import *

#
currentCurrenciesNamespace = Namespace('currencies', description='Namespace to manipulate and get informations about all currencies in the world...')