import os
from flask import render_template, request, redirect, url_for
from flask_classy import FlaskView, route
from gs_app.service.game_service import GameService
from werkzeug.utils import secure_filename
import json
from flask_mongoengine.wtf import model_form
from gs_app.models.games import Game


class GameView(FlaskView):
    route_base = '/'

    @classmethod
    def allowed_file(cls, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in {'png', 'jpg'}

    @route('/games', endpoint='games')
    def home(self):
        games = GameService.get_games()
        return render_template('games.html', games=games)

    @route('/game/<game_uuid>', endpoint='game_details')
    def game_details(self, game_uuid):
        game = GameService.get_games_by_uuid(game_uuid)
        return render_template('game_details.html', game=game)

    @route('/game/add', methods=['GET', 'POST'])
    def add_game(self):
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

            Game(
                name=name,
                price=float(price),
                genre=list_genres,
                image=image_path,
                hide=is_hide,
                description=description
            ).save()

        return render_template('add_game.html')
