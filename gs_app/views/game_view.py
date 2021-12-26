import os
from flask import render_template, request, redirect, url_for
from flask_classy import FlaskView, route
from gs_app.service.game_service import GameService
from werkzeug.utils import secure_filename
from gs_app.models.games import Game, GENRES


class GameView(FlaskView):
    route_base = '/'

    @classmethod
    def allowed_file(cls, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in {'png', 'jpg'}

    @route('/games', endpoint='games', methods=['GET', 'POST'])
    def home(self):
        games = GameService.get_games()

        search = request.args.get('search')
        if search:
            games = GameService.get_games_by_name(search)

        list_of_genres = request.form.getlist('genre')
        if list_of_genres:
            games = GameService.get_games_by_genres(list_of_genres)

        return render_template('games.html', games=games)

    @route('/game/<game_uuid>', endpoint='game_details', methods=['POST', 'GET'])
    def game_details(self, game_uuid):
        game = GameService.get_games_by_uuid(game_uuid)

        file = request.files.get('file')
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('D:/epam_tasks/game_store/gs_app/static/games_logo', filename))
            image_path = 'games_logo/' + filename
            game.update(image=image_path)

        return render_template('game_details.html', game=game, game_uuid=game_uuid)

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

    @route('/game/edit/<game_uuid>', methods=['POST', 'GET'], endpoint='edit_game')
    def edit_game(self, game_uuid):
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
                return 'An error occurred while updating the data.'

        return render_template('edit_game.html', game=game, all_genres=GENRES)
