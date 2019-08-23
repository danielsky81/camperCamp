from django.test import TestCase
from .models import Post, PostComment
from .forms import BlogPostForm, BlogCommentForm


class TestBlogPostForm(TestCase):

    def test_blog_form_validation(self):
        form = BlogPostForm({
            'title': 'A new post',
            'content': 'Some text',
            'tag': 'news'
        })
        self.assertTrue(form.is_valid())

    def test_blog_form_failed_validation(self):
        form = BlogPostForm({
            'title': 'A new post',
            'content': '',
            'tag': 'news'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])


class TestBlogCommentForm(TestCase):

    def test_blog_form_validation(self):
        form = BlogCommentForm({
            'content': 'Some text',
        })
        self.assertTrue(form.is_valid())

    def test_blog_form_failed_validation(self):
        form = BlogCommentForm({
            'content': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])