# Python Imports
import secrets

class Config(object):
    """Based Flask API Configuration"""
    DEBUG = False
    TESTING = False

    SECRET_KEY = secrets.token_urlsafe(64)

    DB_NAME = 'bdCalculator'
    DB_USERNAME = 'bdUser'
    DB_PASSWORD = 'bdPassword'

class ProductionConfig(Config):
    """Production Flask API Configuration"""
    pass

class DevelopmentConfig(Config):
    """Development Flask API Configuration"""
    DEBUG = True

class TestingConfig(Config):
    """Testing Flask API Configuration"""
    TESTING = True
