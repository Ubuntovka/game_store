import os
import datetime
from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_jwt_extended import create_access_token
from flask_login import login_user
# from gs_app.service.game_service import GameService
from werkzeug.utils import secure_filename
from gs_app.models.user import User
from gs_app.service.user_service import UserService


# from gs_app.clean_database.clean_games import CleanGame


class UserView(FlaskView):
    route_base = '/'

    @route('sign_in', methods=['GET', 'POST'])
    def sign_in(self):
        if request.method == 'POST':

            email = request.form.get('email')
            password = request.form.get('password')
            user = User.objects.get(email=email)
            authorized = user.check_password(password)
            if not authorized:
                flash('Email or password invalid')
            else:
                login_user(user)
                flash('Logged in successfully.')

            expires = datetime.timedelta(days=1)

        return render_template('sign_in.html')

    @route('registration', methods=['GET', 'POST'])
    def registration(self):
        if request.method == 'POST':
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            username = request.form.get('username')
            email = request.form.get('email')
            if request.form.get('password') == request.form.get('password2'):
                password = request.form.get('password')
                try:
                    new_user = User(
                        email=email,
                        password=password,
                        firstname=firstname,
                        lastname=lastname,
                        username=username
                    ).save()
                    new_user.hash_password()
                    new_user.save()
                except:
                    return 'An error occurred while adding data.'
            else:
                flash('Enter the same passwords')

        return render_template('registration.html')
