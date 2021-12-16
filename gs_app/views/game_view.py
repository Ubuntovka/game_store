from flask import render_template
from flask_classy import FlaskView, route
from gs_app.service.game_service import GameService


class GameView(FlaskView):
    route_base = '/'

    @route('/games', endpoint='games')
    def home(self):
        games = GameService.get_games()
        return render_template('games.html', games=games)

    @route('/game/<game_uuid>', endpoint='game_details')
    def game_details(self, game_uuid):
        game = GameService.get_games_by_uuid(game_uuid)
        return render_template('game_details.html', game=game)
