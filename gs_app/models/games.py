from gs_app import db
import uuid as u


GENRES = ['Strategy', 'Strategy(Rally)', 'Strategy(Arcade)', 'Strategy(Formula)', 'Strategy(Off-road)', 'RPG', 'Sports',
          'Races', 'Action', 'Action(FPS)', 'Action(TPS)', 'Action(Misc.)', 'Adventure', 'Puzzle & Skill', 'Other']


class Game(db.Document):
    uuid = db.StringField(default=lambda: str(u.uuid4()), unique=True)
    name = db.StringField()
    price = db.FloatField()
    genre = db.ListField(db.StringField())
    image = db.StringField()
    hide = db.BooleanField()
    description = db.StringField()
    hide_change_datetime = db.DateTimeField()

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
            'hide_change_datetime': str(self.hide_change_datetime)
        }
