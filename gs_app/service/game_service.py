"""
Game service used to make database queries, this module defines the
following classes:
- `GameService`, game service
"""

from gs_app.models.game import Game


class GameService:
    """
        Game service used to make database queries
    """

    @staticmethod
    def get_games():
        """
        Fetches all of the games from database
        :return: list of all games
        """
        games = Game.objects(hide=False)
        return games

    @staticmethod
    def get_game_by_uuid(uuid):
        """
        Fetches the game with given UUID from database
        :param uuid: uuid of the game
        :return: game with given uuid
        """
        game = Game.objects(uuid=uuid).first()
        return game

    @staticmethod
    def get_games_by_name(name):
        """
        Fetches the game with given name from database
        :param name: name of the game
        :return: games with given name
        """
        games = Game.objects(name__icontains=name, hide=False)
        return games

    @staticmethod
    def get_games_by_genres(genres: list):
        """
        Fetches all games with at least one genre from list genres
        :param genres: list with genres of the game
        :return: games with given genres
        """
        games = Game.objects(genre__in=genres, hide=False)
        return games

    @staticmethod
    def delete_game_by_uuid(uuid):
        """
        Delete game with given uuid from database
        :param uuid: uuid of the game
        :return: 204
        """
        Game.objects(uuid=uuid).delete()
        return '', 204

    @staticmethod
    def hide_game_by_uuid(uuid):
        """
        Fetches the game with given UUID from database.
        Update `hide` parameter to the game
        :param uuid: uuid of the game
        :return: game with an updated `hide` parameter
        """
        game = Game.objects(uuid=uuid).first()
        if game is None:
            raise ValueError('Invalid game uuid')
        game.update(hide=True)
        return game

