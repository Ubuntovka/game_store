from gs_app.models.game import Game
from gs_app.tests.test_case_base import TestCaseBase


class TestGameApi(TestCaseBase):

    def test_get_games(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        response = self.client.get('/api/games')

        self.assertEqual('name1', response.json[0]['name'])
        self.assertEqual(200, response.status_code)

    def test_get_game_by_uuid(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        response = self.client.get(f'/api/game/{game_1.uuid}')

        self.assertEqual('name1', response.json['name'])
        self.assertEqual(200, response.status_code)
