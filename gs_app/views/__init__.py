"""
This package contains modules defining game services:
Modules:
- `game_view.py`: defines department views
"""

from gs_app import app

from . import game_view, user_view


def init_views():
    """
        Register views
        :return: None
    """
    game_view.GameView.register(app)
    user_view.UserView.register(app)

