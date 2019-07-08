# app/resources/user

# 3rd party imports
from flask_restful import Resource
from flask import request, jsonify

# local imports
from app.models import User

class Login(Resource):
  def post(self):
    user = User.query.filter_by(email=request.data['email']).first()
    if user is not None:
      company_name = request.data['company_name']
      email = request.data['email']
      password = request.data['password']
      user = User(company_name=company_name, email=email)
      user.hash_password(password)
      user.save()


class Signup(Resource):
  def post(self):
    pass

class Logout(Resource):
  def post(self):
    pass

class Users(Resource):
  def get(self):
    return { "greetings": "Hello World" }

  def put(self, user_id):
    pass

  def delete(self, user_id):
    pass

class UsersList(Resource):
  def get(self):
    pass
