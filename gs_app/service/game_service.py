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
        games = Game.objects
        return games

    @staticmethod
    def get_games_by_uuid(uuid):
        game = Game.objects(uuid=uuid).first()
        return game

    @staticmethod
    def get_games_by_name(name):
        games = Game.objects(name__icontains=name)
        return games

    @staticmethod
    def get_games_by_genres(genres: list):
        games = Game.objects(genre__in=genres)
        return games

    @staticmethod
    def delete_game_by_uuid(uuid):
        Game.objects(uuid=uuid).delete()
        return '', 204

