"""

"""

from flask_bcrypt import generate_password_hash
from gs_app.tests.test_case_base import TestCaseBase
from gs_app.models.game import Game
from gs_app.models.user import User
from gs_app.models.cart import Cart
from gs_app.service.cart_service import CartService


class TestCartService(TestCaseBase):
    def test_get_cart_by_game_and_user(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        cart = CartService.get_cart_by_game_and_user(game_1, user_1)
        self.assertEqual(3, cart['quantity'])

    def test_get_cart_by_id(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        cart = CartService.get_cart_by_id(cart_1.pk)
        self.assertEqual(3, cart['quantity'])

    def test_get_list_cart_by_user(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()
        game_2 = Game(
            name='name2',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_2.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        cart_2 = Cart(
            game=game_2,
            user=user_1,
            quantity=3
        )
        cart_2.save()

        list_carts = CartService.get_list_cart_by_user(user_1)
        self.assertEqual(2, len(list_carts))

    def test_get_total_cost_by_current_user(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        cost = CartService.get_total_cost_by_current_user(user_1)
        self.assertEqual(75.0, cost)

    def test_delete_cart_obj_by_cart_id(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        CartService.delete_cart_obj_by_cart_id(cart_1.pk)
        self.assertEqual(0, len(CartService.get_list_cart_by_user(user_1)))

    def test_add_one_to_quantity(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        CartService.add_one_to_quantity(cart_1.pk)
        cart = CartService.get_cart_by_id(cart_1.pk)
        self.assertEqual(4, cart['quantity'])

    def test_subtract_one_to_quantity(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        cart_1 = Cart(
            game=game_1,
            user=user_1,
            quantity=3
        )
        cart_1.save()

        CartService.subtract_one_to_quantity(cart_1.pk)
        cart = CartService.get_cart_by_id(cart_1.pk)
        self.assertEqual(2, cart['quantity'])
