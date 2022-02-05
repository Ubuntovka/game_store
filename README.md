# Game Store

## With this app you can:
### As a guest:
- View the catalog of available games.
- Registration.
- See the full description of the game.
- Search games by name and filter by genre.

### As a user:
- Login.
- Edit your profile.
- Add/delete/edit cart entries.
- Add/delete/edit comments.
- Reply to comments from other users.
- Place an order from the shopping cart.

### As a manager:
- Delete user comments.
- Add/remove/edit games.
- Change game status to hidden.

### As a admin:
- Grant permissions to users.

## How to build this project:

- ### Install the requirements:
```
pip install -r requirements.txt
```
- ### Configure MongoDB

- ### Set the following environment variables:

```
PSWRD_DB_SERVER = your password from database server 

MONGODB_DB = name of your database
MONGODB_HOST = your host
MONGODB_PORT = your port
```

*You can set these in .env file as the project uses dotenv module to load 
environment variables*

- ### Optionally populate the database with sample data
```
python -m gs_app/database/populate.py
python -m gs_app/database/create_users.py
```

- ### Run the project locally:
```
python -m flask run
```

## Now you should be able to access the web service and web application on the following addresses:

- ### Web Service:
```
localhost:5000/api/games
localhost:5000/api/game/<uuid>
localhost:5000/api/auth/signup
localhost:5000/api/auth/login
```

- ### Web Application:
```
localhost:5000/
localhost:5000/games
localhost:5000/game/<game_uuid>
localhost:5000/game/add
localhost:5000/game/edit/<game_uuid>
localhost:5000/game/delete/<game_uuid>
localhost:5000/game/edit_comment/<comment_id>
localhost:5000/game/reply_comment/<comment_id>
localhost:5000/game/delete_comment/<comment_id>
localhost:5000/cart
localhost:5000/cart/add/<game_uuid>
localhost:5000/cart/delete/<cart_obj_id>
localhost:5000/cart/add_quantity/<cart_obj_id>
localhost:5000/cart/subtract_quantity/<cart_obj_id>
localhost:5000/cart/order
localhost:5000/order
localhost:5000/order/confirm
localhost:5000/admin/permissions
localhost:5000/admin/to_manager/<user_id>
localhost:5000/admin/to_user/<user_id>
localhost:5000/sign_in
localhost:5000/registration
localhost:5000/logout
localhost:5000/user
localhost:5000/user/edit
```