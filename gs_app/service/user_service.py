"""
User service used to make database queries, this module defines the
following classes:
- `UserService`, user service
"""

from gs_app.models.user import User


class UserService:

    @staticmethod
    def get_user_by_email(user_email):
        """
        Fetches a user with given user email from database
        :param user_email: user email
        :return: user with given user email
        """
        user = User.objects(email=user_email).first()
        return user

    @staticmethod
    def add_user(json_data):
        """
        Add user with given json_data to database
        :param json_data: json data with info about new user
        :return: new user with given json data
        """
        new_user = User(
            email=json_data["email"],
            password=json_data["password"],
            firstname=json_data["firstname"],
            lastname=json_data["lastname"],
            username=json_data["username"]
        ).save()
        new_user.hash_password()
        new_user.save()
        return new_user

    @staticmethod
    def login_user(json_data):
        """
        Log in as a user with given json data
        :param json_data: json data with info about user
        :return: user object or 401
        """
        user = User.objects.get(email=json_data.get('email'))
        authorized = user.check_password(json_data.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        else:
            return user

