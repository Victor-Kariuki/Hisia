# app/models.py

# inbuilt imports
from datetime import datetime
from uuid import uuid4

# 3rd party imports
from passlib.apps import custom_app_context as pwd_context

# local imports
from app import db

class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  uuid = db.Column(db.Integer, default=uuid4().hex)
  username = db.Column(db.String(32), index=True, unique=True)
  email = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  is_admin = db.Column(db.Boolean, default=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, username, email):
    self.username = username;
    self.email = email;

  def hash_password(self, password):
    self.password_hash = pwd_context.encrypt(password)

  def verify_password(self, password):
    return pwd_context.verify(password, self.password_hash)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def repr(self):
    return '<user: {}>'.format(self.username)

