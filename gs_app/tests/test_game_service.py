from gs_app.models.game import Game
from gs_app.tests.test_case_base import TestCaseBase
from gs_app.service.game_service import GameService


class TestGameService(TestCaseBase):
    def test_get_games(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()
        games = GameService.get_games()
        self.assertEqual('name1', games[0]['name'])

    def test_get_games_by_uuid(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        game = GameService.get_game_by_uuid(game_1.uuid)

        self.assertEqual('name1', game['name'])

    def test_get_games_by_name(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        games = GameService.get_games_by_name('na')
        self.assertEqual('name1', games[0]['name'])

    def test_get_games_by_genres(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()
        game_2 = Game(
            name='name2',
            price=25,
            genre=['RPG', 'Action', 'Sports'],
            hide=False
        )
        game_2.save()

        games = GameService.get_games_by_genres(['RPG', 'Action'])
        self.assertEqual('name1', games[0]['name'])
        self.assertEqual('name2', games[1]['name'])

    def test_delete_game_by_uuid(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()
        game_2 = Game(
            name='name2',
            price=25,
            genre=['RPG', 'Action', 'Sports'],
            hide=False
        )
        game_2.save()

        GameService.delete_game_by_uuid(game_2.uuid)
        games = GameService.get_games()

        self.assertEqual(1, len(games))

    def test_hide_game_by_uuid(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        GameService.hide_game_by_uuid(game_1.uuid)
        game = GameService.get_game_by_uuid(game_1.uuid)

        self.assertEqual(True, game.hide)