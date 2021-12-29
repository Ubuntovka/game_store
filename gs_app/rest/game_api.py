"""
Departments REST API, this module defines the following classes:
- `GameApiBase`, game API base class
- `GameListApi`, game list API class
- `GameApi`, game API class
"""

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
        """
        GET request handler of game list API
        Fetches all games and returns them in a JSON format
        with a status code 200(OK)
        :return: a list of all departments JSON and a status code 200
        """
        games = self.service.get_games()
        return [game.to_dict() for game in games], 200


class GameApi(GameApiBase):
    """
    Game API class
    """

    def get(self, uuid):
        """
        GET request handler of game API
        Fetches the game with given uuid game and returns it in a
        JSON format with a status code 200(OK)
        :return: a tuple of the department with given uuid in JSON and a status
        code 200
        """
        game = self.service.get_games_by_uuid(uuid)
        return game.to_dict(), 200

    def delete(self, uuid):
        game = self.service.delete_game_by_uuid(uuid)
        return game
