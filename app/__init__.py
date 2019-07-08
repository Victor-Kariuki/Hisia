# api/__init__.py

# third-party imports
from flask import Flask, json, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import tweepy

# local imports
from config import app_config

# resources imports
from app.resources import Users

# Initialize the imports
db = SQLAlchemy()

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  api = Api(app)

  db.init_app(app)

  Migrate(db, app)

  from app.models import User, Location, Search, SearchDetail

  # create flask shell
  @app.shell_context_processor
  def make_shell_context():
    return dict(app=app, db=db, User=User, Location=Location, Search=Search, SearchDetail=SearchDetail)

  # register resources
  api.add_resource(Users, '/api/v1/users')

  return app
