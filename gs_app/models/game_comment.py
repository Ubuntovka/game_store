import uuid as u
from gs_app import db
from .user import User
from .game import Game


class Comment(db.Document):
    uuid = db.StringField(default=lambda: str(u.uuid4()), unique=True)
    user = db.ReferenceField(User)
    game = db.ReferenceField(Game)
    comment = db.StringField(max_lenght=600)
    parent_comment_uuid = db.StringField()
    time = db.DateTimeField()

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'uuid': self.uuid,
            'user': self.user,
            'game': self.game,
            'comment': self.comment,
            'parent_comment_id': self.parent_comment_uuid,
            'time': str(self.time)
        }
