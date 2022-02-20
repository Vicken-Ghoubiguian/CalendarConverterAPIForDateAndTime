#
from tokenize import String
from flask import Flask, request
from flask_restx import Api, Resource, reqparse
from datetime import datetime
from pytz import timezone

#
app = Flask(__name__)

#
api = Api(app)

#
date_and_time_template = "%Y-%m-%d %H:%M:%S"

#
@api.route('/hello')
class HelloWorld(Resource):

    #
    def get(self):
        return {"Message": "Hello, world!"}, 200

#
@api.route('/currentDateTime/<string:choosen_timezone>')
class CurrentDateTimeByTimezone(Resource):

    #
    def get(self, choosen_timezone):

        #
        now_utc = datetime.now(timezone('UTC'))

        #
        choosen_timezone = choosen_timezone.replace("&", "/")

        #
        now_from_timezone = now_utc.astimezone(timezone(choosen_timezone))

        #
        return {"time": now_from_timezone.strftime(date_and_time_template), "timezone": choosen_timezone}, 200

#
if __name__ == '__main__':
    
    #
    app.run()
