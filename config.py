# config.py

class Config():
  '''
    Global configurations
  '''
  TESTING = False
  DEBUG = False

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

