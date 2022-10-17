#
from flask_restx import Namespace, Resource, inputs

#
from commonFunctions import *

#
introductionNamespace = Namespace('introduction', description='')

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