"""
Game views used to manage games on web application, this module
defines the following classes:
- `GameView`, class that defines game views
"""

import os
import datetime
from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_login import login_required, current_user
from gs_app.service.game_service import GameService
from werkzeug.utils import secure_filename
from gs_app.models.game import Game, GENRES
from gs_app import manager_permission

# from gs_app.clean_database.clean_games import CleanGame


class GameView(FlaskView):
    """
       Game views used to manage games on web application
    """

    # base url route for all department routes
    route_base = '/'

    @classmethod
    def allowed_file(cls, filename):
        """
        Method `allowed_file` used to check the file extension.
        :param filename:str File name.
        :return: bool, True if file extension valid.
        """
        return '.' in filename and filename.rsplit('.', 1)[1] in {'png', 'jpg'}

    @route('/games', endpoint='games', methods=['GET', 'POST'])
    def home(self):
        """
        Returns rendered `games.html` template for url route
        `/games` and endpoint `games`
        :return: rendered `games.html` template
        """
        games = GameService.get_games()

        # CleanGame.clean_game_by_hide()

        search = request.args.get('search')
        if search:
            games = GameService.get_games_by_name(search)

        list_of_genres = request.form.getlist('genre')
        if list_of_genres:
            games = GameService.get_games_by_genres(list_of_genres)

        return render_template('games.html', games=games, all_genres=GENRES)

    @route('/game/<game_uuid>', endpoint='game_details', methods=['POST', 'GET'])
    def game_details(self, game_uuid):
        """
         Returns rendered `game_details.html` template for url route
        `/game/<game_uuid>` and endpoint `game_details`
        :param game_uuid:str game uuid
        :return: rendered `game_details.html` template
        """
        game = GameService.get_games_by_uuid(game_uuid)

        if request.method == "POST":
            # Get information about the button to hide / open the game
            if request.form.get('hide_game') == 'True':
                game.update(hide=True, hide_change_datetime=datetime.datetime.utcnow())
            elif request.form.get('hide_game') == 'False':
                game.update(hide=False, hide_change_datetime=None)

            # Get path to file with image games and add to database
            file = request.files.get('file')
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join('D:/epam_tasks/game_store/gs_app/static/games_logo', filename))
                image_path = 'games_logo/' + filename
                game.update(image=image_path)

            return redirect('/game/' + game_uuid)

        return render_template('game_details.html', game=game, game_uuid=game_uuid)

    @login_required
    @manager_permission.require()
    @route('/game/add', methods=['GET', 'POST'])
    def add_game(self):
        """
        Returns rendered `add_game.html` template for url route
        `/game/add`
        :return: rendered `add_game.html` template
        """
        if request.method == 'POST':
            name = request.form.get('name')

            price = request.form.get('price')
            if not price:
                price = 0

            list_genres = request.form.getlist('genre')

            file = request.files.get('file')
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join('D:/epam_tasks/game_store/gs_app/static/games_logo', filename))
                image_path = 'games_logo/' + filename
            else:
                image_path = None

            is_hide = bool(request.form.get('hide'))

            description = request.form.get('description')
            try:
                Game(
                    name=name,
                    price=float(price),
                    genre=list_genres,
                    image=image_path,
                    hide=is_hide,
                    description=description
                ).save()
            except:
                return 'An error occurred while adding data.'
        return render_template('add_game.html', all_genres=GENRES)

    @login_required
    @manager_permission.require()
    @route('/game/edit/<game_uuid>', methods=['POST', 'GET'], endpoint='edit_game')
    def edit_game(self, game_uuid):
        """
        Returns rendered `edit_game.html` template for url route
        `/game/edit/<game_uuid>`
        :param game_uuid:str game uuid
        :return: rendered `edit_game.html` template
        """
        game = GameService.get_games_by_uuid(game_uuid)
        if request.method == 'POST':

            name = request.form.get('name')

            price = request.form.get('price')
            if not price:
                price = 0

            list_genres = request.form.getlist('genre')

            file = request.files.get('file')
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join('D:/epam_tasks/game_store/gs_app/static/games_logo', filename))
                image_path = 'games_logo/' + filename
            else:
                image_path = game.image

            is_hide = bool(request.form.get('hide'))

            description = request.form.get('description')

            try:
                game.update(
                    name=name,
                    price=float(price),
                    genre=list_genres,
                    image=image_path,
                    hide=is_hide,
                    description=description
                )
                return redirect('/game/' + game_uuid)
            except:
                flash('An error occurred while updating the data.')

        return render_template('edit_game.html', game=game, all_genres=GENRES)
