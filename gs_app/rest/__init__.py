from gs_app import api

from . import game_api


def init_api():
    """
    Register REST Api endpoints
    :return: None
    """
    api.add_resource(
        game_api.GameListApi,
        '/api/games'
    )
    api.add_resource(
        game_api.GameApi,
        '/api/game/<uuid>'
    )
