from gs_app import db
from gs_app.models.games import Game


class GameService:
    """
        Department service used to make database queries
    """

    @classmethod
    def get_games(cls):
        """
        :return: list of all games
        """
        games = Game.objects
        return games
