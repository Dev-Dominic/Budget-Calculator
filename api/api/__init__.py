# Flask Imports
from flask import Flask

# Loading environment variables
from dotenv import load_dotenv
load_dotenv()

# Setting up flask application and current working environemtn type
app = Flask(__name__)

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from . import endpoints
