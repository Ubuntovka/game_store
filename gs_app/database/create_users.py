from flask_bcrypt import generate_password_hash
from gs_app import user_datastore


def create_user():
    manager_role = user_datastore.find_or_create_role(name='manager', description='Manager role')
    user = user_datastore.create_user(
        email='manager@example.com',
        password=generate_password_hash('asdf1234').decode('utf8'),
        roles=[manager_role]
    )
    user_datastore.add_role_to_user(user, manager_role)


if __name__ == '__main__':
    print('Populating database...')
    create_user()
    print('Successfully populated')