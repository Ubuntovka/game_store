from gs_app import db
from gs_app.models.games import Game


class GameService:
    """
        Department service used to make database queries
    """

    @staticmethod
    def get_games():
        """
        :return: list of all games
        """
        games = Game.objects()
        return games

    @staticmethod
    def get_games_by_uuid(uuid):
        game = Game.objects(uuid=uuid).first()
        return game

