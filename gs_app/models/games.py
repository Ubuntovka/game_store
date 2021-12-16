from gs_app import db
import uuid as u


class Game(db.Document):
    uuid = db.StringField(default=lambda: str(u.uuid4()), unique=True)
    name = db.StringField()
    price = db.FloatField()
    genre = db.ListField()
    image = db.StringField()
    hide = db.BooleanField()
    description = db.StringField()

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'uuid': self.uuid,
            'name': self.name,
            'price': self.price,
            'genre': self.genre,
            'image': self.image,
            'hide': self.hide,
            'description': self.description
        }
