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

db = MongoEngine()
db.init_app(app)

api = Api(app)

from .rest import init_api
init_api()

from .views import init_views
init_views()

from .models import games

# from .clean_database import clean_games
