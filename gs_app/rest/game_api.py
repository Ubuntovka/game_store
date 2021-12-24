from flask_restful import Resource
from flask import json, jsonify

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
        return [game.to_dict() for game in games], 200


class GameApi(GameApiBase):
    """
    Game API class
    """

    def get(self, uuid):
        game = self.service.get_games_by_uuid(uuid)
        return game.to_dict(), 200

    def delete(self, uuid):
        game = self.service.delete_game_by_uuid(uuid)
        return game
