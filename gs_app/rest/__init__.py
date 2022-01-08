"""
This package contains modules defining game REST APIs and
functions to initialize respective API endpoints:
Modules:
- `game_api.py`: defines model representing games
Functions:
- `init_api`: register REST API endpoints
"""

from gs_app import api

from . import game_api, user_api


def init_api():
    """
    Register REST Api endpoints
    :return: None
    """
    api.add_resource(
        game_api.GameListApi,
        '/api/games'
    )
    api.add_resource(
        game_api.GameApi,
        '/api/game/<uuid>'
    )
    api.add_resource(
        user_api.SignupApi,
        '/api/auth/signup'
    )
    api.add_resource(
        user_api.LoginApi,
        '/api/auth/login'
    )
