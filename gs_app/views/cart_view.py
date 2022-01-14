from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_login import login_required, current_user
from gs_app.models.cart import Cart
from gs_app.service.game_service import GameService
from gs_app.service.cart_service import CartService
from gs_app.models.game import Game, GENRES
from gs_app.models.game_comment import Comment
from gs_app import manager_permission


class CartView(FlaskView):
    """
    Cart views used to manage carts on web application
    """

    # base url route for all department routes
    route_base = '/'

    @login_required
    @route('/cart', methods=['POST', 'GET'])
    def cart(self):

        return None

    @login_required
    @route('/cart/add/<game_uuid>', endpoint='add_in_cart', methods=['POST', 'GET'])
    def add_in_cart(self, game_uuid):
        exist_cart = CartService.get_cart_by_game_and_user(GameService.get_games_by_uuid(game_uuid), current_user)
        if exist_cart:
            exist_cart.update(
                quantity=exist_cart.quantity + 1
            )
        else:
            new_cart = Cart(
                game=GameService.get_games_by_uuid(game_uuid),
                user=current_user,
                quantity=1
            )
            new_cart.save()
        return render_template('add_in_cart.html', game=GameService.get_games_by_uuid(game_uuid))
