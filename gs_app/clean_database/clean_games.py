import datetime

from gs_app.models.games import Game


class CleanGame:

    @staticmethod
    def clean_game_by_hide():
        games_hide_true = Game.objects(hide=True)

        for game in games_hide_true:
            datetime_hide = game.hide_change_datetime
            difference_between_datetime = datetime.datetime.utcnow() - datetime_hide
            if difference_between_datetime.days > 90:
                game.delete()

