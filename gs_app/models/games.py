from gs_app import db


class Game(db.Document):
    name = db.StringField()
    price = db.FloatField()
    genre = db.ListField()
    image = db.StringField()
    hide = db.BooleanField()
    description = db.StringField()


