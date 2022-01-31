"""
Cart model used to represent parts of carts, this module defines the
following classes:
- `Cart`, cart model
"""

from gs_app import db
from .game import Game
from .user import User


class Cart(db.Document):
    """
    Model representing cart
    """
    game = db.ReferenceField(Game)
    user = db.ReferenceField(User)
    quantity = db.IntField(max_value=1001, min_value=1)
    is_order = db.BooleanField(default=False)

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'game': self.game,
            'user': self.user,
            'quantity': self.quantity,
            'is_order': self.is_order
        }
