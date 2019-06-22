# app/resources/user

# 3rd party imports
from flask.views import MethodView
from flask import request, jsonify

# local imports
from app.models import User

class Login(MethodView):
  def post(self):
    user = User.query.filter_by(email=request.data['email']).first()
    if user is not None:
      try:
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user = User(username=username, email=email)
        user.hash_password(password)
        user.save()



class Signup(MethodView):
  def post(self):
    pass

class Users(MethodView):
  def get(self):
    return { "greetings": "Hello World" }

  def put(self, user_id):
    pass

  def delete(self, user_id):
    pass

class UsersList(MethodView):
  def get(self):
    pass
