"""
Game comment service used to make database queries, this module defines the
following classes:
- `CommentService`, game comment service
"""

from gs_app.models.game_comment import Comment


class CommentService:

    @staticmethod
    def get_comments_by_game(game):
        """
        Fetches all of the comments with given game from database
        :param game: game object
        :return: comments with given game
        """
        comments = Comment.objects(game=game.pk).all()
        return comments

    @staticmethod
    def get_comment_by_id(comment_id):
        """
        Fetches a comment with given comment_id from database
        :param comment_id: comment id
        :return: comment object
        """
        comment = Comment.objects(id=comment_id).first()
        return comment

    @staticmethod
    def delete_comment_by_id(comment_id):
        """
        Delete comment with given id from database
        :param comment_id: comment id
        :return: 204
        """
        Comment.objects(id=comment_id).delete()
        return '', 204

    @staticmethod
    def get_comments_by_uuid(comment_uuid):
        """
        Fetches a comment with comment uuid from database
        :param comment_uuid: comment uuid
        :return: comment object
        """
        comment = Comment.objects(uuid=comment_uuid).first()
        return comment
