# config.py

# inbuilt imports
import os

class Config():
  '''
    Global configurations
  '''
  TESTING = False
  DEBUG = False
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
  SQLALCHEMY_ECHO = True
  SECRET_KEY = os.getenv('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  '''
    Production env configs
  '''

class DevelopmentConfig(Config):
  '''
    Development env configs
  '''

  DEBUG = True

class TestingConfig(Config):
  '''
    Testing env configs
  '''

  TESTING = True

app_config = {
  'production': ProductionConfig,
  'development': DevelopmentConfig,
  'testing': TestingConfig,
}

