# app/schemas.py

# local imports
from app import ma

class UserSchema(ma.Schema):
  '''
  create user schema
  '''
  class Meta:
    fields= ('uuid', 'company_name', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
