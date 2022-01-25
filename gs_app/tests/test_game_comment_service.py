from gs_app.tests.test_case_base import TestCaseBase
from gs_app.models.game_comment import Comment
from gs_app.service.game_comment_service import CommentService
from gs_app.models.game import Game


class TestGameCommentService(TestCaseBase):
    def test_get_comments_by_game(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        Comment(
            game=game_1,
            comment='some comment'
        ).save()

        comment = CommentService.get_comments_by_game(game_1)
        self.assertEqual('some comment', comment[0]['comment'])

    def test_get_comment_by_id(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        comment_1 = Comment(
            game=game_1,
            comment='some comment'
        )
        comment_1.save()

        comment = CommentService.get_comment_by_id(comment_1.pk)
        self.assertEqual('some comment', comment['comment'])

    def test_delete_comment_by_id(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        comment_1 = Comment(
            game=game_1,
            comment='some comment'
        )
        comment_1.save()

        CommentService.delete_comment_by_id(comment_1.pk)
        comments = CommentService.get_comments_by_game(game_1)
        self.assertEqual(0, len(comments))

    def test_get_comment_by_uuid(self):
        game_1 = Game(
            name='name1',
            price=25,
            genre=['RPG', 'Action', 'Adventure', 'Other'],
            hide=False
        )
        game_1.save()

        comment_1 = Comment(
            game=game_1,
            comment='some comment'
        )
        comment_1.save()

        comment = CommentService.get_comment_by_uuid(comment_1.uuid)
        self.assertEqual('some comment', comment['comment'])
