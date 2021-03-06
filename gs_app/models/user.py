"""
User model used to represent users, this module defines the
following classes:
- `User`, user model
- `Role`, role model
"""

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_security import RoleMixin
from gs_app import db, login_manager


class Role(db.Document, RoleMixin):
    """
    Model representing role
    """
    name = db.StringField(unique=True)
    description = db.StringField()


class User(db.Document, UserMixin):
    """
    Model representing user
    """
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8)
    firstname = db.StringField()
    lastname = db.StringField()
    username = db.StringField()
    image = db.StringField()
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'email': self.email,
            'password': self.password,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'image': self.image
        }


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(id=user_id)
