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
    '''
    authenticate user
    '''
    user = User.query.filter_by(email=request.get_json().get('email')).first()
    password = request.get_json().get('password')
    if user is not None and user.verify_password(password):
      '''
      checks if user exists and verifies the password
      '''
      token = user.generate_auth_token()
      result = user_schema.dump(user).data
      response = {
        'status': 'Success',
        'data': result,
        'token': token.decode('ascii'),
        'message': 'Successfully Logged In. Welcome to Hisia'
      }
      return response, 200
    else:
      '''
      returns an error message if the user doesn't exists
      '''
      response = {
        'status': 'Failed',
        'data': result,
        'message': 'User does not exists. Please Register'
      }
      return response, 400



class Signup(Resource):
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

class Profile(Resource):
  def get(self):
    users = User.get_all()
    users = users_schema.dump(users).data


  def put(self, user_id):
    pass

  def delete(self, user_id):
    pass

class Users(Resource):
  def get(self):
    users = User.get_all()
    users = users_schema.dump(users).data
    return {'status': 'success', 'data': users}, 200
