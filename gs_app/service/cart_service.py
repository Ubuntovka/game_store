"""
Cart service used to make database queries, this module defines the
following classes:
- `CartService`, cart service
"""

from gs_app.models.cart import Cart


class CartService:
    """
    Cart service used to make database queries
    """

    @staticmethod
    def get_cart_by_game_and_user(game, user):
        """
        Fetches a cart with given game and user from database
        :param game: the game from cart
        :param user: user whose cart
        :return: cart with given game and user
        """
        cart = Cart.objects(game=game, user=user, is_order=False).first()
        return cart

    @staticmethod
    def get_cart_by_id(cart_id):
        cart = Cart.objects(id=cart_id).first()
        return cart

    @staticmethod
    def get_list_cart_by_user(user):
        """
        Fetches all carts with given user from database
        :param user: user whose cart
        :return: carts with given user
        """
        list_cart = Cart.objects(user=user, is_order=False).all()
        return list_cart

    @staticmethod
    def get_total_cost_by_current_user(user):
        """
        Fetches total cost with given user from database
        :param user: user whose cart
        :return: total cost with given user
        """
        total = 0.0
        for i in Cart.objects(user=user, is_order=False).all():
            total += i.game.price * i.quantity
        return total

    @staticmethod
    def delete_cart_obj_by_cart_id(cart_id):
        """
        Delete cart with given cart_id from database
        :param cart_id: cart id
        :return: 204
        """
        Cart.objects(id=cart_id).delete()
        return '', 204

    @staticmethod
    def add_one_to_quantity(cart_id):
        """
        Add one point to cart.quantity with given cart_id
        :param cart_id: cart id
        :return: cart
        """
        cart_obj = Cart.objects(id=cart_id).first()
        cart_obj.update(
            quantity=cart_obj.quantity + 1
        )
        return cart_obj

    @staticmethod
    def subtract_one_to_quantity(cart_id):
        """
        Subtract one point from cart.quantity with given cart_id
        :param cart_id: cart id
        :return: cart
        """
        cart_obj = Cart.objects(id=cart_id).first()
        cart_obj.update(
            quantity=cart_obj.quantity - 1
        )
        return cart_obj


