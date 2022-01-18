"""
Game model used to represent games, this module defines the
following classes:
- `Game`, game model
"""

from gs_app import db
import uuid as u

# All genres that the game can have
GENRES = ['Strategy', 'Strategy(Rally)', 'Strategy(Arcade)', 'Strategy(Formula)', 'Strategy(Off-road)', 'RPG', 'Sports',
          'Races', 'Action', 'Action(FPS)', 'Action(TPS)', 'Action(Misc.)', 'Adventure', 'Puzzle & Skill', 'Other']


class Game(db.Document):
    """
    Model representing game
    """
    uuid = db.StringField(default=lambda: str(u.uuid4()), unique=True)
    name = db.StringField()
    price = db.FloatField()
    genre = db.ListField(db.StringField())
    image = db.StringField()
    hide = db.BooleanField()
    description = db.StringField()
    hide_change_datetime = db.DateTimeField()
    licenses = db.IntField(default=7858772994, max_value=7858772994, min_value=0)

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'uuid': self.uuid,
            'name': self.name,
            'price': self.price,
            'genre': self.genre,
            'image': self.image,
            'hide': self.hide,
            'description': self.description,
            'hide_change_datetime': str(self.hide_change_datetime),
            'licenses': self.licenses
        }
