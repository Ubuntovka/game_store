from flask_restful import Resource

from gs_app.service.game_service import GameService


class GameApiBase(Resource):
    """
    Game API base class
    """
    # game database service
    service = GameService()


class GameListApi(GameApiBase):
    """
    Games list API class
    """
    def get(self):
        games = self.service.get_games()
        return games
