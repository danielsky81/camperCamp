from django.test import TestCase
from .models import Post, PostComment
from django.contrib.auth.models import User

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(
            author_id = 1,
            title = 'First Post',
            content = 'Some content',
            tag = 'news'
        )

    def test_post_name_is_post_title(self):
        post = Post.objects.get(id=1)
        expected_post_name = post.title
        self.assertEquals(expected_post_name, str(post))


class PostCommentModelTest(TestCase):
    def setUp(self):
        User.objects.create(
            username='Ed'
        )
        Post.objects.create(
            author_id = 1,
            title = 'First Post',
            content = 'Some content',
            tag = 'news'
        )
        PostComment.objects.create(
            post_id=1,
            author_id = 1,
            content = 'Some comment'
        )

    def test_post_comment_name_is_post_comment_title_and_username(self):
        comment = PostComment.objects.get(id=1)
        expected_comment_name = 'Comment on %s by %s' % (comment.post.title, comment.author.username)
        self.assertEquals(expected_comment_name, str(comment))