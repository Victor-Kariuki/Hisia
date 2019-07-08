# app/models.py

# inbuilt imports
from datetime import datetime, timedelta
from uuid import uuid4
import os

# 3rd party imports
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# local imports
from app import db

class User(db.Model):
  '''
  creates users table
  '''

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  uuid = db.Column(db.Integer, default=uuid4().hex)
  company_name = db.Column(db.String(32), index=True, unique=True)
  email = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  date_created = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, company_name, email):
    self.company_name = company_name
    self.email = email

  def hash_password(self, password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def generate_token(self, id):
    try:
      payload = {
        'exp': datetime.utcnow() + timedelta(minutes=5),
        'iat': datetime.utcnow(),
        'sub': id
      }
      jwt_string = jwt.encode(
        payload,
        os.getenv('SECRET_KEY'),
        algorithm='HS256'
      )
      return jwt_string
    except Exception as e:
      return str(e)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def repr(self):
    return '<user: {}>'.format(self.username)

  @staticmethod
  def decode_token(token):
    try:
      payload = jwt.decode(token, os.getenv('SECRET_KEY'))
      return payload['sub']
    except jwt.ExpiredSignatureError:
      return "Expired token. Please login to get a new token"
    except jwt.InvalidTokenError:
      return "Invalid token. Please register or login"



class Location(db.Model):
  '''
  create locations table
  '''

  __tablename__ = 'locations'

  id = db.Column(db.Integer, primary_key=True)
  country = db.Column(db.String(64))
  postal_town = db.Column(db.String(64))
  postal_code = db.Column(db.String(64))
  postal_address = db.Column(db.String(64))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Search(db.Model):
  '''
  create searches table
  '''
  __tablename__ = 'searches'

  id = db.Column(db.Integer, primary_key=True)
  search_results_id = db.Column(db.Integer, db.ForeignKey('search_details.id'))
  company_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class SearchDetail(db.Model):
  '''
  create search details table
  '''
  __tablename__ = 'search_details'

  id = db.Column(db.Integer, primary_key=True)
  params = db.Column(db.String(128))
  result = db.Column(db.String(64))

