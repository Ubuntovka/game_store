from flask import render_template, request, redirect, url_for, flash
from flask_classy import FlaskView, route
from flask_login import login_required, current_user
from gs_app import admin_permission
from gs_app.service.user_service import UserService
from gs_app.models.user import User
from gs_app.models.user import Role


class AdminView(FlaskView):
    """
       Admin views used to manage admin on web application
    """

    # base url route for all routes
    route_base = '/'

    @admin_permission.require()
    @route('/admin/permissions', endpoint='admin_permissions', methods=['GET', 'POST'])
    def admin_permissions(self):
        search = request.args.get('search')
        if search:
            user = UserService.get_user_by_email(search)
        else:
            user = None

        return render_template('admin_permission.html', user=user)

    @admin_permission.require()
    @route('/admin/to_manager/<user_id>', endpoint='user_to_manager', methods=['GET', 'POST'])
    def user_to_manager(self, user_id):
        user = User.objects(id=user_id).first()
        user.update(
            roles=[Role.objects(name='manager').first()]
        )
        return redirect('/admin/permissions')

    @admin_permission.require()
    @route('/admin/to_user/<user_id>', endpoint='to_user', methods=['GET', 'POST'])
    def to_user(self, user_id):
        user = User.objects(id=user_id).first()
        user.update(
            roles=None
        )
        return redirect('/admin/permissions')
