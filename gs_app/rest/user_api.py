from flask import request
from gs_app.models.user import User
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token
from gs_app.service.user_service import UserService


class SignupApi(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        new_user = UserService.add_user(json_data)
        id = new_user.id
        return {'id': str(id)}, 200


class LoginApi(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        user = UserService.login_user(json_data)
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
