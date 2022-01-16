from gs_app.models.cart import Cart


class CartService:

    @staticmethod
    def get_cart_by_game_and_user(game, user):
        cart = Cart.objects(game=game, user=user, is_order=False).first()
        return cart

    @staticmethod
    def get_list_cart_by_user(user):
        list_cart = Cart.objects(user=user, is_order=False).all()
        return list_cart

    @staticmethod
    def get_total_cost_by_current_user(user):
        total = 0.0
        for i in Cart.objects(user=user, is_order=False).all():
            total += i.game.price * i.quantity
        return total

    @staticmethod
    def delete_cart_obj_by_cart_id(cart_id):
        Cart.objects(id=cart_id).delete()
        return '', 204

    @staticmethod
    def add_one_to_quantity(cart_id):
        cart_obj = Cart.objects(id=cart_id).first()
        cart_obj.update(
            quantity=cart_obj.quantity + 1
        )
        return cart_obj

    @staticmethod
    def subtract_one_to_quantity(cart_id):
        cart_obj = Cart.objects(id=cart_id).first()
        cart_obj.update(
            quantity=cart_obj.quantity - 1
        )
        return cart_obj


