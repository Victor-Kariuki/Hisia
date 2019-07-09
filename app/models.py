# app/models.py

# inbuilt imports
from datetime import datetime, timedelta
from uuid import uuid4
import os

# 3rd party imports
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

# local imports
from app import db

class User(db.Model):
  '''
  creates users table
  '''

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  uuid = db.Column(db.String(128), default=uuid4().hex, nullable=False)
  company_name = db.Column(db.String(32), index=True, unique=True, nullable=False)
  email = db.Column(db.String(64), unique=True, index=True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, company_name, email, password):
    self.company_name = company_name
    self.email = email
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def generate_auth_token(self, expiration = 600):
    s = Serializer(os.getenv('SECRET_KEY'), expires_in=expiration)
    return s.dumps({ 'id': self.id })

  def save(self):
    db.session.add(self)
    db.session.commit()

  def repr(self):
    return '<user: {}>'.format(self.username)

  @staticmethod
  def verify_token(token):
    s = Serializer(os.getenv('SECRET_KEY'))
    try:
      data = s.loads(token)
    except SignatureExpired:
      return "Expired token. Please login to get a new token"
    except BadSignature:
      return "Invalid token. Please register or login"
    user = User.query.get(data['id'])
    return user


class Location(db.Model):
  '''
  create locations table
  '''

  __tablename__ = 'locations'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  country = db.Column(db.String(64), nullable=False)
  postal_town = db.Column(db.String(64), nullable=False)
  postal_code = db.Column(db.String(64), nullable=False)
  postal_address = db.Column(db.String(64), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Search(db.Model):
  '''
  create searches table
  '''
  __tablename__ = 'searches'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  search_results_id = db.Column(db.Integer, db.ForeignKey('search_details.id'))
  company_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class SearchDetail(db.Model):
  '''
  create search details table
  '''
  __tablename__ = 'search_details'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  params = db.Column(db.String(128))
  result = db.Column(db.String(64))

