"""
The flask application package.
"""
from flask import Flask
from flask_restful import Api
from eyula_restapi_test.utils.json_encoder import MyEncoder
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import datetime
import os

load_dotenv()

app = Flask(__name__)

jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = str(os.getenv("JWT_SECRET_KEY"))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

app.json_encoder = MyEncoder

# register api
api = Api(app)

#register blueprints
from .customers import customers_bp
from .companies import companies_bp

app.register_blueprint(customers_bp)
app.register_blueprint(companies_bp)

import eyula_restapi_test.views
