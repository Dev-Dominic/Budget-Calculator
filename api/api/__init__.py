# Flask Imports
from flask import Flask

# PyPI Imports
from pymongo import MongoClient

# Loading environment variables
from dotenv import load_dotenv
load_dotenv()

# Setting up flask application and current working environment type
# Setting up mongodb database client
app = Flask(__name__)
db_client = MongoClient(os.getenv('MONGO_URI'))

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from api import endpoints
