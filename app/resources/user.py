# app/resources/user

#inbuilt imports

# 3rd party imports
from flask_restful import Resource
from flask import request, jsonify

# local imports
from app.models import User
from app.schemas import user_schema, users_schema

class Login(Resource):
  def post(self):
    user = User.query.filter_by(email=request.get_json().get('email')).first()
    if user is not None:
      company_name = request.get_json().get('company_name')
      email = request.get_json().get('email')
      password = request.get_json().get('password')
      user = User(company_name=company_name, email=email)
      user.hash_password(password)
      user.save()
      token = user.generate_token(user.uuid)


class Signup(Resource):
  def get(self):
    return {'message': 'Hello World'}

  def post(self):
    '''
    create a new user
    '''
    user = User.query.filter_by(email=request.get_json().get('email')).first()
    if user is None:
      '''
      if email doesn't exist create a new users
      '''
      try:
        company_name = request.get_json().get('company_name')
        email = request.get_json().get('email')
        password = request.get_json().get('password')
        user = User(company_name=company_name, email=email, password=password)
        user.save()
        token = user.generate_auth_token()
        result = user_schema.dump(user).data
        response = {
          'status': 'Success',
          'data': result,
          'token': token.decode('ascii'),
          'message': 'Successfully register. Please Login'
        }
        return response, 201
      except Exception as e:
        return {'message': str(e)}, 400
    else:
      '''
      if users exists return a 403 error
      '''
      result = user_schema.dump(user).data
      response = {
        'status': 'Failed',
        'data': result,
        'message': 'User already exists. Please login'
      }
      return response, 403

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
