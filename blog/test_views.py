from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, PostComment
from django.shortcuts import get_object_or_404, reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage 


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='Joe', password='dummypassword')
        self.client.login(username='Joe', password='dummypassword')
        post = Post.objects.create(
            author_id = 1,
            title = 'First Post',
            content = 'Some content',
            tag = 'news'
        )

    def test_get_posts_page(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_get_posts_view_by_tag_type(self):
        post_tag = Post.objects.filter(tag='issue')
        response = self.client.get('/blog/tag_issues/')
        self.assertEqual(response.status_code, 200)
        post_tag = Post.objects.filter(tag='feature')
        response = self.client.get('/blog/tag_features/')
        self.assertEqual(response.status_code, 200)
        post_tag = Post.objects.filter(tag='news')
        response = self.client.get('/blog/tag_news/')
        self.assertEqual(response.status_code, 200)
        post_tag = Post.objects.filter(tag='other')
        response = self.client.get('/blog/tag_other/')
        self.assertEqual(response.status_code, 200)

    def test_get_post_detail_view(self):
        post = get_object_or_404(Post, pk=1)
        self.assertEqual(post.views, 0)
        response = self.client.get(reverse('post_detail', kwargs={'pk': '1'})) 
        post.views += 1 
        post.save()
        self.assertEqual(post.views, 1)
        self.assertEqual(response.status_code, 200)


class TestAdminViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='admin', password='password', is_superuser=True)
        self.client.login(username='admin', password='password')

    def test_create_new_post(self):
        pk = None
        post = get_object_or_404(Post, pk=pk) if pk else None 
        self.assertEqual(Post.objects.count(), 0)
        response = self.client.post(reverse('new_post'), {
            'author_id': '1',
            'title': 'First Post',
            'content': 'Some content',
            'tag': 'news'
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get(reverse('post_detail', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_post_form_display(self):
        response = self.client.get(reverse('new_post'))
        self.assertEqual(response.status_code, 200)

    def test_user_is_not_superuser(self):
        user_other = User.objects.create_user(username='Joe', password='dummypassword', is_superuser=False)
        self.client.login(username='Joe', password='dummypassword')
        self.assertEqual(user_other.is_superuser, False)
        response = self.client.post(reverse('new_post'), {
            'author_id': '1',
            'title': 'First Post',
            'content': 'Some content',
            'tag': 'news'
            })
        self.assertRedirects(response, '/blog/', 302)

    def test_update_post(self):
        post = Post.objects.create(
            author_id = 1,
            title = 'First Post',
            content = 'Some content',
            tag = 'news'
        )
        response = self.client.post(reverse('edit_post', kwargs={'pk': '1'}), {
            'author_id': '1',
            'title': 'First Post',
            'content': 'Some content',
            'tag': 'other'
            })
        post.tag = 'other'
        post.updated_date = timezone.now()
        post.save()
        self.assertEqual(post.tag, 'other')
        self.assertEqual(response.status_code, 302)

    def test_delete_post(self):
        post = Post.objects.create(
            author_id = 1,
            title = 'First Post',
            content = 'Some content',
            tag = 'news'
        )
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get(reverse('delete_post', kwargs={'pk': '1'}))
        post.delete()
        self.assertEqual(Post.objects.count(), 0)
        self.assertRedirects(response, '/blog/', 302)
        
class TestCommentsViews(TestCase):

    def setUp(self):
        admin = User.objects.create_user(username='admin', password='password', is_superuser=True)
        user = User.objects.create_user(username='Joe', password='dummypassword')
        post = Post.objects.create(
            author_id = 1,
            title = 'First Post',
            content = 'Some content',
            tag = 'news'
        )
        self.client.login(username='Joe', password='dummypassword')

    def test_add_new_comment(self):
        post = get_object_or_404(Post, pk=1)
        response = self.client.post(reverse('add_comment_to_post', kwargs={'pk': '1'}), {
            'author_id': '2',
            'post_id': '1',
            'content': 'Some text'
            })
        self.assertEqual(response.status_code, 302)

    def test_add_new_comment_form_display(self):
        response = self.client.get(reverse('add_comment_to_post', kwargs={'pk': '1'})) 
        self.assertEqual(response.status_code, 200)

    def test_update_existing_comment(self):
        comment = PostComment.objects.create(
            post_id=1,
            author_id=2,
            content='Some content'
        ) 
        response = self.client.post(reverse('edit_comment_post', kwargs={'pk': '1'}), {
            'author_id': '2',
            'content': 'Some edited content'
            })
        self.assertEqual(response.status_code, 302)

    def test_edit_comment_form_display(self):
        comment = PostComment.objects.create(
            post_id=1,
            author_id=2,
            content='Some content'
        ) 
        response = self.client.get(reverse('edit_comment_post', kwargs={'pk': '1'})) 
        self.assertEqual(response.status_code, 200)

    def test_delete_post_comment(self):
        comment = PostComment.objects.create(
            author_id = 2,
            post_id=1,
            content = 'Some comment',
        )
        self.assertEqual(PostComment.objects.count(), 1)
        response = self.client.get(reverse('delete_comment_post', kwargs={'pk': '1'}))
        comment.delete()
        self.assertEqual(PostComment.objects.count(), 0)
        self.assertRedirects(response, '/blog/', 302)
