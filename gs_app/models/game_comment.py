import datetime
from gs_app import db
from .user import User
from .game import Game


class Comment(db.Document):
    user = db.ReferenceField(User)
    game = db.ReferenceField(Game)
    comment = db.StringField(max_lenght=600)
    parent_comment_id = db.StringField()
    time = db.DateTimeField()

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'user': self.user.username,
            'game': self.game.name,
            'comment': self.comment,
            'parent_comment_id': self.parent_comment_id,
            'time': str(self.time)
        }
