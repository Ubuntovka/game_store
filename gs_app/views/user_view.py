from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_login import login_user, logout_user, login_required, current_user
from gs_app.models.user import User
from gs_app.service.user_service import UserService


class UserView(FlaskView):
    route_base = '/'

    @route('sign_in', methods=['GET', 'POST'])
    def sign_in(self):
        if request.method == 'POST':

            email = request.form.get('email')
            password = request.form.get('password')
            if email and password:
                user = User.objects(email=email).first()
                if user:
                    authorized = user.check_password(password)
                    if authorized:
                        remember = request.form.get('remember')
                        if bool(remember):
                            login_user(user, remember=True)
                        else:
                            login_user(user)
                        return redirect('/games')
                    else:
                        flash('Invalid password')
                else:
                    flash('Invalid email')

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
                    flash('An error occurred while adding data.')
            else:
                flash('Enter the same passwords')

        return render_template('registration.html')

    @route('/logout', methods=['GET', 'POST'])
    @login_required
    def logout(self):
        logout_user()
        flash('You were logged out')
        return redirect('/games')
