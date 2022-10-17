#
from flask_restx import Namespace, Resource, inputs

#
from commonFunctions import *

#
introductionNamespace = Namespace('introduction', description='Namespace to introduce, present and explain all functionalities of the DateTime API...')

#
@introductionNamespace.route('/presentation')
class Presentation(Resource):

    #
    def get(self):

        """
        Get a presentation of the DateTime API...
        """

        #
        return "", 200