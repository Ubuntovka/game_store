"""
This package contains modules defining game services:
Modules:
- `game_view.py`: defines department views
- `user_view.py`: defines user views
- `cart_view.py`: defines cart views
"""

from gs_app import app

from . import game_view, user_view, cart_view, admin_view


def init_views():
    """
        Register views
        :return: None
    """
    game_view.GameView.register(app)
    user_view.UserView.register(app)
    cart_view.CartView.register(app)
    admin_view.AdminView.register(app)


from . import error
