# Python Imports
import secrets


class Config(object):
    """Base Flask API Configuration"""
    DEBUG = False
    TESTING = False

    SECRET_KEY = secrets.token_urlsafe(64)


class ProductionConfig(Config):
    """Production Flask API Configuration"""
    pass

class DevelopmentConfig(Config):
    """Development Flask API Configuration"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Flask API Configuration"""
    TESTING = True
