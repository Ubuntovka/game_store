from gs_app.models.game_comment import Comment


class CommentService:

    @staticmethod
    def get_comments_by_game(game):
        comments = Comment.objects(game=game.pk).all()
        return comments

    @staticmethod
    def get_comment_by_id(comment_id):
        comment = Comment.objects(id=comment_id).first()
        return comment

    @staticmethod
    def delete_comment_by_id(comment_id):
        Comment.objects(id=comment_id).delete()
        return '', 204

    @staticmethod
    def get_comments_by_uuid(comment_uuid):
        comment = Comment.objects(uuid=comment_uuid).first()
        return comment
