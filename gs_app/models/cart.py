from gs_app import db
from .game import Game
from .user import User


class Cart(db.Document):
    game = db.ReferenceField(Game)
    user = db.ReferenceField(User)
    quantity = db.IntField()
    is_order = db.BooleanField()

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'game': self.game,
            'user': self.user,
            'quantity': self.quantity,
            'is_order': self.is_order
        }
