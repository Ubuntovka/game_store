"""
This module contains class for clean database.
Classes:
- `CleanGame`, clean games which have hide status more then 90 days.
"""

import datetime
from gs_app.models.game import Game


class CleanGame:
    """
    Class for clean game by hide field.
    Methods:
        - `clean game by hide`, delete game by hide
    """

    @staticmethod
    def clean_game_by_hide():
        """
        Delete game if hide more then 90 days.
        :return: None
        """
        games_hide_true = Game.objects(hide=True)

        for game in games_hide_true:
            datetime_hide = game.hide_change_datetime
            difference_between_datetime = datetime.datetime.utcnow() - datetime_hide
            if difference_between_datetime.days > 90:
                game.delete()

        return None
