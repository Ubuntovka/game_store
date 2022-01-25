import http
from gs_app.models.game import Game
from gs_app.service.game_service import GameService
from gs_app.tests.test_case_base import TestCaseBase


class TestGameView(TestCaseBase):
    def test_games(self):
        response = self.client.get('/games')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    # def test_game_details(self):
    #     game_1 = Game(
    #         name='name1',
    #         price=25,
    #         genre=['RPG', 'Action', 'Adventure', 'Other'],
    #         hide=False
    #     )
    #     game_1.save()
    #     game_uuid = GameService.get_game_by_uuid(game_1.uuid)
    #     response = self.client.get(f'/game/{game_uuid}')
    #     # self.assertEqual('name1', response.data)
    #     self.assertEqual(response.status_code, http.HTTPStatus.OK)

