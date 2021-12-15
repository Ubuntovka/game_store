from gs_app import app

from . import game_view


def init_views():
    game_view.GameView.register(app)
