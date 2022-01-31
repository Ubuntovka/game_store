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

from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
import datetime
from flask_principal import Permission, RoleNeed
from flask_security import MongoEngineUserDatastore, Security
from config import DevelopmentConfig

# from flask_mail import Mail, Message

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

app.config['REMEMBER_COOKIE_DURATION'] = datetime.timedelta(days=7)

# database
db = MongoEngine()
db.init_app(app)

# mail
# mail = Mail(app)

# RESTful API
api = Api(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Create a permission with a single Need, in this case a RoleNeed.
admin_permission = Permission(RoleNeed('admin'))
manager_permission = Permission(RoleNeed('manager'))
admin_manager_permission = Permission(RoleNeed('admin'), RoleNeed('manager'))

from .rest import init_api

init_api()

from .views import init_views

init_views()

from .models import game, user

# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, user.User, user.Role)
security = Security(app, user_datastore)

# from .clean_database import clean_games
