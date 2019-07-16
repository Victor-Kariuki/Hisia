# app/resources/message.py

# 3rd party imports
from flask_restful import Resource
from flask import request, jsonify

# local imports
from app.models import Message
from app.schemas import message_schema, messages_schema

class Text(Resource):
  def post(self):
    '''
    create a new message
    '''

    email = request.get_json().get('email')
    message = request.get_json().get('message')

    if (email is not None and message is not None):
      try:
        new_message = Message(email, message)
        new_message.save()
        result = message_schema.dump(new_message).data
        response = {
          'status': 'Successful',
          'data': result,
          'message': 'Message successfully sent'
        }
        return response, 201

      except Exception as e:
        response = {
          'status': 'Failed',
          'data': e,
          'message': 'Message not sent'
        }

        return response, 400

      response = {
        'status': 'Failed',
        'message': 'Cannot send empty message'
      }

      return response, 400

