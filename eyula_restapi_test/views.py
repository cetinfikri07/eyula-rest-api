"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from eyula_restapi_test import app
from eyula_restapi_test import api
from flask_restful import Resource
import json
from flask import jsonify

class HelloWorld(Resource):
    def get(self):
        print(app.url_map)
        return jsonify({"hello":"world"})

api.add_resource(HelloWorld,"/")






