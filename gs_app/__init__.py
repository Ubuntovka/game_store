"""
Sources root package.
Initializes web application and web service, contains following subpackages and
modules:
Subpackages:
- `clean_database` contains modules used to clean records from database
- `database`: contains modules used to populate database
- `models`: contains modules with Python classes describing database models
- `rest`: contains modules with RESTful service implementation
- `service`: contains modules with classes used to work with database
- `static`: contains web application static files (scripts, styles, images)
- `templates`: contains web application html templates
- `views`: contains modules with web controllers/views
- `tests`: contains modules with unit tests
"""

from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

app.config['MONGODB_SETTINGS'] = {
    'db': 'game_store',
    'host': 'localhost',
    'port': 27017
}

# database
db = MongoEngine()
db.init_app(app)

# RESTful API
api = Api(app)

from .rest import init_api

init_api()

from .views import init_views

init_views()

from .models import games

# from .clean_database import clean_games
