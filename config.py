import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "allan2327,."

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config_environments = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}