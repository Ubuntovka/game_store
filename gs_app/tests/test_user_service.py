from flask_bcrypt import generate_password_hash
from gs_app.tests.test_case_base import TestCaseBase
from gs_app.models.user import User
from gs_app.service.user_service import UserService


class TestUserService(TestCaseBase):
    def test_get_user_by_email(self):
        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        user = UserService.get_user_by_email(user_1.email)
        self.assertEqual('asdf@gamil.com', user.email)

    def test_add_user(self):
        UserService.add_user(
            {
                'email': 'asdf@gamil.com',
                'password': 'qwer1234',
                'firstname': 'yuri',
                'lastname': 'katsuki',
                'username': 'kauri'
            }
        )
        user = UserService.get_user_by_email('asdf@gamil.com')
        self.assertEqual('asdf@gamil.com', user.email)

    def test_login_user(self):
        user_1 = User(
            email='asdf@gamil.com',
            password=generate_password_hash('asdf1234').decode('utf8')
        )
        user_1.save()

        user = UserService.login_user(
            {
                'email': 'asdf@gamil.com',
                'password': 'asdf1234'
            }
        )
        self.assertEqual(user_1, user)