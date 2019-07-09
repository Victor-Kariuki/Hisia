# api/__init__.py

# third-party imports
from flask import Flask, json, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import tweepy

# local imports
from config import app_config

# Initialize the imports
db = SQLAlchemy()

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  api = Api(app)

  db.init_app(app)
  migrate = Migrate(app=app, db=db)

  from app.models import User, Location, Search, SearchDetail

  # create flask shell
  @app.shell_context_processor
  def make_shell_context():
    return dict(app=app, db=db, User=User, Location=Location, Search=Search, SearchDetail=SearchDetail)

  # resources imports
  from app.resources.user import Users, Login, Signup, Logout, UsersList

  # register resources
  api.add_resource(Users, '/api/v1/users')
  api.add_resource(Login, '/api/v1/login')
  api.add_resource(Signup, '/api/v1/signup')
  api.add_resource(Logout, '/api/v1/logout')

  return app
