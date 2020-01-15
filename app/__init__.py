import sys
from flask import Flask, redirect, url_for, request, render_template
from flask_restplus import Resource, Api, reqparse
from werkzeug.exceptions import BadRequest
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


application = Flask(__name__)
application.config.from_object(Config)
cors = CORS(application)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
api = Api(application,
          version='0.1',
          title='Contender Ranking REST API',
          description='REST-ful API',
)

from app import routes, models

