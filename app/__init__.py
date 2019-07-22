# api/__init__.py

# third-party imports
from flask import Flask, json, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import tweepy

# local imports
from config import app_config

# Initialize the imports
db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  api = Api(app)

  db.init_app(app)
  migrate = Migrate(app=app, db=db)

  ma.init_app(app)

  cors.init_app(app)

  from app.models import User, Location, Search, SearchDetail, Message

  # create flask shell
  @app.shell_context_processor
  def make_shell_context():
    return dict(
      app=app, db=db, User=User, Location=Location, Search=Search, SearchDetail=SearchDetail, Message=Message,
    )

  # resources imports
  from app.resources.user import Users, Login, Register, Logout, Profile
  from app.resources.message import Text
  from app.resources.streamer import Tweets

  # register resources
  api.add_resource(Users, '/api/v1/users', endpoint = 'users')
  api.add_resource(Profile, '/api/v1/users/<string:uuid>', endpoint='user')
  api.add_resource(Login, '/api/v1/login')
  api.add_resource(Register, '/api/v1/register')
  api.add_resource(Logout, '/api/v1/logout')
  api.add_resource(Text, '/api/v1/contact')
  api.add_resource(Tweets, '/api/v1/tweets')

  return app
