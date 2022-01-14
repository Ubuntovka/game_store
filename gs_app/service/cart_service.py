from gs_app.models.cart import Cart


class CartService:

    @staticmethod
    def get_cart_by_game_and_user(game, user):
        cart = Cart.objects(game=game, user=user).first()
        return cart
