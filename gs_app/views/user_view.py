import os
from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from gs_app.models.user import User
from gs_app.service.user_service import UserService


class UserView(FlaskView):
    route_base = '/'

    @classmethod
    def allowed_file(cls, filename):
        """
        Method `allowed_file` used to check the file extension.
        :param filename:str File name.
        :return: bool, True if file extension valid.
        """
        return '.' in filename and filename.rsplit('.', 1)[1] in {'png', 'jpg'}

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

    @route('/user', methods=['GET', 'POST'])
    @login_required
    def user_info(self):
        return render_template('user.html')

    @route('/user/edit', methods=['GET', 'POST'])
    @login_required
    def user_edit(self):
        user = UserService.get_game_by_email(current_user.email)
        if request.method == 'POST':
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            username = request.form.get('username')

            file = request.files.get('file')
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join('D:/epam_tasks/game_store/gs_app/static/user_images', filename))
                image_path = 'user_images/' + filename
            else:
                image_path = user.image

            try:
                user.update(
                    email=email,
                    firstname=firstname,
                    lastname=lastname,
                    username=username,
                    image=image_path
                )
                return redirect('/user')
            except:
                flash('An error occurred while updating the data.')

        return render_template('edit_user.html')
