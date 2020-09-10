# Python Imports
import os

# PyPI Imports
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

# Configuration Import
from api.lib import create_mongo_client

# Setting up flask application and current working environment type
# Setting up mongodb database client
app = Flask(__name__)

client = None
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
    client = create_mongo_client(os.getenv('MONGO_URI_PRODUCTION'))
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
    client = create_mongo_client('', testing=True)
else:
    app.config.from_object('config.DevelopmentConfig')
    client = create_mongo_client(os.getenv('MONGO_URI_DEVELOPMENT'))

if bool(client) is False:
    raise Exception('MongoDB Client not setup')

from api import endpoints
