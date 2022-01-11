from gs_app.models.user import User


class UserService:

    @staticmethod
    def get_game_by_email(user_email):
        user = User.objects(email=user_email).first()
        return user

    @staticmethod
    def add_user(json_data):
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
        user = User.objects.get(email=json_data.get('email'))
        authorized = user.check_password(json_data.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        else:
            return user

