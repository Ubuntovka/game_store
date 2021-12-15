from flask import render_template
from flask_classy import FlaskView, route
from gs_app.rest.game_api import GameListApi


class GameView(FlaskView):
    route_base = '/'

    @route('/games', endpoint='games')
    def home(self):
        games = GameListApi().get()
        return render_template('games.html', games=games)

    @route('/game_details')
    def game_details(self):
        return render_template('game_detail.html')
