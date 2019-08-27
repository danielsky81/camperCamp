from django.test import TestCase
from .models import Items, ItemComments, Votes
from django.contrib.auth.models import User

class ItemsModelTest(TestCase):

    def setUp(self):
        Items.objects.create(
            author_id = 1,
            title = 'Item',
            description = 'Some description',
            views = 0,
            votes = 0,
            category = 'new',
            item_type = 'issue',
        )

    def test_profile_name_is_first_name_surname(self):
        item = Items.objects.get(id=1)
        expected_item_name = '{0} - {1} : {2}'.format(item.item_type, item.category, item.title)
        self.assertEquals(expected_item_name, str(item))


class ItemCommentsModelTest(TestCase):

    def setUp(self):
        User.objects.create(
            id=1,
            username='Joe'
        )
        Items.objects.create(
            author_id = 1,
            title = 'Item',
            description = 'Some description',
            views = 0,
            votes = 0,
            category = 'new',
            item_type = 'issue',
        )
        ItemComments.objects.create(
            author_id = 1,
            item_id = 1,
            content = 'Some Content'
        )

    def test_profile_name_is_first_name_surname(self):
        comment = ItemComments.objects.get(id=1)
        expected_item_comment_name = 'Comment on {0} by {1}'.format(comment.item.title, comment.author.username)
        self.assertEquals(expected_item_comment_name, str(comment))


class VotesModelTest(TestCase):

    def setUp(self):
        User.objects.create(
            id=1,
            username='Joe'
        )
        Items.objects.create(
            author_id = 1,
            title = 'Item',
            description = 'Some description',
            views = 0,
            votes = 0,
            category = 'new',
            item_type = 'issue',
        )
        Votes.objects.create(
            voted_item_id = 1,
            user_id = 1,
            votes_number = 0,
        )

    def test_profile_name_is_first_name_surname(self):
        vote = Votes.objects.get(id=1)
        expected_votes_name = '{0} - {1}'.format(vote.user, vote.votes_number) 
        self.assertEquals(expected_votes_name, str(vote))