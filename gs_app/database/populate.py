from gs_app.models.game import Game


def populate_database():
    Game(
        name='The Witcher 3',
        price=25,
        genre=['RPG', 'Action', 'Adventure', 'Other'],
        image='games_logo/the_witcher_3.jpg',
        hide=False,
        description='As war rages on throughout the Northern Realms, you take on the greatest contract of your'
                    ' life — tracking down the Child of Prophecy, a living weapon that can alter the shape'
                    ' of the world.',
        licenses=1000000
    ).save()
    Game(
        name='Cyberpunk 2077',
        price=20,
        genre=['RPG', 'Action(FPS)', 'Adventure', 'Other'],
        image='games_logo/cyberpunk.jpg',
        hide=False,
        description='Cyberpunk 2077 is an open-world, action-adventure story set in Night City, a megalopolis'
                    ' obsessed with power, glamour and body modification. You play as V, a mercenary outlaw going'
                    ' after a one-of-a-kind implant that is the key to immortality.',
        licenses=1000000
    ).save()
    Game(
        name='Dark Souls 3',
        price=49,
        genre=['RPG', 'Action', 'Adventure', 'Other'],
        image='games_logo/dark_souls_3.jpg',
        hide=False,
        description='Dark Souls continues to push the boundaries with the latest, ambitious chapter in '
                    'the critically-acclaimed and genre-defining series. Prepare yourself and Embrace The Darkness!',
        licenses=1000000
    ).save()


if __name__ == '__main__':
    print('Populating database...')
    populate_database()
    print('Successfully populated')
