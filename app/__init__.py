# app/__init__.py

# third-party imports
from flask import Flask, json, request
from flask_restful import Resource, Api
import tweepy

# local imports
from config import app_config

def create_app(env_name):
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  api = Api(app)

  class HelloWorld(Resource):
    def get(self):
      return { 'hello': 'world' }

  api.add_resource(HelloWorld, '/')


  return app
