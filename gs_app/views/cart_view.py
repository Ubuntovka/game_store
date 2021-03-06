from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_login import login_required, current_user
from gs_app.models.cart import Cart
from gs_app.models.order import Order
from gs_app.service.game_service import GameService
from gs_app.service.cart_service import CartService
from gs_app import manager_permission


class CartView(FlaskView):
    """
    Cart views used to manage carts on web application
    """

    # base url route for all routes
    route_base = '/'

    @login_required
    @route('/cart', endpoint='cart', methods=['POST', 'GET'])
    def cart(self):
        user = current_user
        cart = CartService.get_list_cart_by_user(user)
        total = CartService.get_total_cost_by_current_user(user)
        return render_template('cart.html', cart=cart, total=total)

    @login_required
    @route('/cart/add/<game_uuid>', endpoint='add_in_cart', methods=['POST', 'GET'])
    def add_in_cart(self, game_uuid):
        exist_cart = CartService.get_cart_by_game_and_user(GameService.get_game_by_uuid(game_uuid), current_user)
        game = GameService.get_game_by_uuid(game_uuid)
        if game.licenses > 0:
            if exist_cart:
                try:
                    exist_cart.update(
                        quantity=exist_cart.quantity + 1,
                    )
                except:
                    flash('This is the maximum quantity of a product that you can order.')
            else:
                new_cart = Cart(
                    game=GameService.get_game_by_uuid(game_uuid),
                    user=current_user,
                    quantity=1
                )

                game.update(
                    licenses=game.licenses - 1
                )
                new_cart.save()
        else:
            flash('Unfortunately, this game is currently out of stock.')
        return render_template('add_in_cart.html', game=GameService.get_game_by_uuid(game_uuid))

    @login_required
    @route('/cart/delete/<cart_obj_id>', endpoint='cart_delete', methods=['POST', 'GET'])
    def delete_cart(self, cart_obj_id):
        CartService.delete_cart_obj_by_cart_id(cart_obj_id)
        return redirect('/cart')

    @login_required
    @route('/cart/add_quantity/<cart_obj_id>', endpoint='cart_add_quantity', methods=['POST', 'GET'])
    def add_quantity(self, cart_obj_id):
        cart = CartService.get_cart_by_id(cart_obj_id)
        game = GameService.get_game_by_uuid(cart.game.uuid)
        if game.licenses > 0:
            try:
                CartService.add_one_to_quantity(cart_obj_id)
            except:
                flash('This is the maximum quantity of a product that you can order.')
            game.update(
                licenses=game.licenses - 1
            )
        else:
            flash('Unfortunately, this game is currently out of stock.')
        return redirect('/cart')

    @login_required
    @route('/cart/subtract_quantity/<cart_obj_id>', endpoint='cart_subtract_quantity', methods=['POST', 'GET'])
    def subtract_quantity(self, cart_obj_id):
        cart = CartService.get_cart_by_id(cart_obj_id)
        game = GameService.get_game_by_uuid(cart.game.uuid)
        if game.licenses > 0:
            if cart.quantity > 1:
                CartService.subtract_one_to_quantity(cart_obj_id)
                game.update(
                    licenses=game.licenses + 1
                )
            else:
                return redirect(url_for('cart_delete', cart_obj_id=cart_obj_id))
        else:
            flash('Unfortunately, this game is currently out of stock.')
        return redirect('/cart')

    @login_required
    @route('/cart/order', endpoint='cart_order', methods=['POST', 'GET'])
    def cart_order(self):
        if request.method == 'POST':
            first_name = request.form.get('firstname')
            last_name = request.form.get('lastname')
            email = request.form.get('email')
            phone = request.form.get('phone')
            payment_type = request.form.get('payment_type')
            comment = request.form.get('comment')

            try:
                Order(
                    cart=CartService.get_list_cart_by_user(current_user),
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    payment_type=payment_type,
                    comment=comment
                ).save()
            except:
                return 'An error occurred while adding data.'
            finally:
                return redirect('/order')

        return render_template('order.html')

    @login_required
    @route('/order', endpoint='order', methods=['POST', 'GET'])
    def order(self):
        cart = CartService.get_list_cart_by_user(current_user)
        total = CartService.get_total_cost_by_current_user(current_user)
        return render_template('submit_order.html', cart=cart, total=total)

    @login_required
    @route('/order/confirm', endpoint='order_confirm', methods=['POST', 'GET'])
    def confirm_order(self):
        last_cart = CartService.get_list_cart_by_user(current_user)
        for i in last_cart:
            i.update(
                is_order=True
            )
        return redirect('/games')
