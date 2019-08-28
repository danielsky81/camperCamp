from django.test import TestCase
from .models import Items, ItemComments, Votes
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Joe',
            password='dummypassword'
        )
        issue = Items.objects.create(
            author_id=1,
            title='issue',
            description='Some description',
            views=0,
            votes=0,
            category='new',
            item_type='issue',
        )
        feature = Items.objects.create(
            author_id=1,
            title='feature',
            description='Some description',
            views=0,
            votes=0,
            category='new',
            item_type='feature',
        )
        comment = ItemComments.objects.create(
            author_id=1,
            item_id=1,
            content='Some Content'
        )

    def test_get_issues_page_view(self):
        response = self.client.get('/items/issues/')
        self.assertEqual(response.status_code, 200)

    def test_get_features_page_view(self):
        response = self.client.get('/items/features/')
        self.assertEqual(response.status_code, 200)

    def test_get_items_detail_view(self):
        item = get_object_or_404(Items, pk=1)
        item.views += 1
        item.save()
        response = self.client.get(reverse('item_detail', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_create_new_issue(self):
        pk = None
        item = get_object_or_404(Items, pk=pk) if pk else None
        self.assertEqual(Items.objects.count(), 2)
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        response = self.client.post(reverse('new_issue'), {
            'author_id': '1',
            'title': 'issue',
            'description': 'Some description',
            'views': '0',
            'votes': '0',
            'category': 'new',
            'item_type': 'issue',
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Items.objects.count(), 3)

    def test_create_new_issue_form_display(self):
        response = self.client.get(reverse('new_issue'))
        self.assertEqual(response.status_code, 200)

    def test_create_new_feature(self):
        pk = None
        feature = get_object_or_404(Items, pk=pk) if pk else None
        self.assertEqual(Items.objects.count(), 2)
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        response = self.client.post(reverse('new_feature'), {
            'author_id': '1',
            'title': 'issue',
            'description': 'Some description',
            'views': '0',
            'votes': '0',
            'category': 'new',
            'item_type': 'feature',
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Items.objects.count(), 3)

    def test_create_new_feature_form_display(self):
        response = self.client.get(reverse('new_feature'))
        self.assertEqual(response.status_code, 200)

    def test_update_existing_items(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        item = get_object_or_404(Items, pk=1)
        item.updated_date = timezone.now()
        item.save()
        response = self.client.get(reverse('edit_item', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_add_new_comment(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        item = get_object_or_404(Items, pk=1)
        response = self.client.post(reverse('add_comment_to_item', kwargs={'pk': '1'}), {
            'author_id': '1',
            'item_id': '1',
            'content': 'Some text'
            })
        self.assertEqual(response.status_code, 302)

    def test_add_new_comment_form_display(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        item = get_object_or_404(Items, pk=1)
        response = self.client.get(reverse('add_comment_to_item', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_update_existing_comment(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        comment = get_object_or_404(ItemComments, pk=1)
        response = self.client.post(reverse('edit_comment_item', kwargs={'pk': '1'}), {
            'author_id': '1',
            'content': 'Some edited content'
            })
        self.assertEqual(response.status_code, 302)

    def test_edit_comment_form_display(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        comment = get_object_or_404(ItemComments, pk=1)
        response = self.client.get(reverse('edit_comment_item', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_delete_post_comment(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        comment = get_object_or_404(ItemComments, pk=1)
        self.assertEqual(ItemComments.objects.count(), 1)
        response = self.client.get(reverse('delete_comment_item', kwargs={'pk': '1'}))
        comment.delete()
        self.assertEqual(ItemComments.objects.count(), 0)
        self.assertRedirects(response, '/items/1/', 302)

    def test_add_vote_to_issue(self):
        user = User.objects.create_user(
            username='Adam',
            password='password'
        )
        self.client.login(
            username='Adam',
            password='password'
        )
        item = get_object_or_404(Items, pk=1)
        votes = Votes.objects.filter(voted_item=item)
        user = User.objects.get(username='Adam')
        response = self.client.post(reverse('add_vote', kwargs={'pk': '1'}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_vote_to_issue_if_already_voted(self):
        user = User.objects.create_user(
            username='Adam',
            password='password'
        )
        self.client.login(
            username='Adam',
            password='password'
        )
        item = get_object_or_404(Items, pk=1)
        votes = Votes.objects.filter(voted_item=item)
        user = User.objects.get(username='Adam')
        vote = Votes(
            voted_date=timezone.now(),
            user=user,
            voted_item=item
        )
        vote.votes_number = 1
        vote.save()
        item.votes += 1
        item.save()
        response = self.client.post(reverse('add_vote', kwargs={'pk': '1'}), follow=True)
        self.assertEqual(response.status_code, 200)

    def add_vote_to_feature(self):
        user = User.objects.create_user(
            username='Adam',
            password='password'
        )
        self.client.login(
            username='Adam',
            password='password'
        )
        item = get_object_or_404(Items, pk=2)
        user = User.objects.get(username='Adam')
        vote = Votes(
            voted_date=timezone.now(),
            user=user,
            voted_item=item,
            votes_number=0
        )
        response = self.client.get(reverse('item_detail', kwargs={'pk': '2'}))
        votes_number = vote.votes_number
        session = self.client.session
        session['feature'] = 2
        session['votes_number'] = votes_number
        session.save()
        response = self.client.post(reverse('add_vote', kwargs={'pk': '2'}),  {
            'votes_number': 'votes_number'
        })
        self.assertRedirects(response, '/items/2/checkout/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_admin_update_category_display(self):
        user = User.objects.create_user(
            username='admin',
            password='password',
            is_superuser=True
        )
        self.client.login(
            username='admin',
            password='password'
        )
        item = get_object_or_404(Items, pk=1)
        item.category = 'done'
        response = self.client.get(reverse('admin_update', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_admin_update_category(self):
        user = User.objects.create_user(
            username='admin',
            password='password',
            is_superuser=True
        )
        self.client.login(
            username='admin',
            password='password'
        )
        item = get_object_or_404(Items, pk=1)
        response = self.client.post(reverse('admin_update', kwargs={'pk': '1'}), {
            'author_id': '1',
            'title': 'issue',
            'description': 'Some description',
            'views': '0',
            'votes': '0',
            'category': 'done',
            'item_type': 'issue',
            })
        self.assertEqual(response.status_code, 302)

    def test_update_category_by_regular_user(self):
        self.client.login(
            username='Joe',
            password='dummypassword'
        )
        item = get_object_or_404(Items, pk=1)
        item.category = 'done'
        response = self.client.get(reverse('admin_update', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 302)
