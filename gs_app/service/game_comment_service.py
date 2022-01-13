from gs_app.models.game_comment import Comment


class CommentService:

    @staticmethod
    def get_comments_by_game(game):
        comments = Comment.objects(game=game.pk).all()
        return comments

    @staticmethod
    def get_game_by_id(comment_id):
        comment = Comment.objects(id=comment_id).first()
        return comment
