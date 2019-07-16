# app/schemas.py

# local imports
from app import ma

class UserSchema(ma.Schema):
  '''
  create user schema
  '''
  class Meta:
    fields = ('uuid', 'company_name', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class MessageSchema(ma.Schema):
  '''
  create messages schema
  '''
  class Meta:
    fields = ('email', 'message')

message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)

class SearchSchema(ma.Schema):
  '''
  create a searchs schema
  '''

  class Meta:
    fields = ()
