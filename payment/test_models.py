from django.test import TestCase
from .models import Transaction
from accounts.models import Profile
from items.models import Items
from django.contrib.auth.models import User

class TransactionModelTest(TestCase):

    def setUp(self):
        Profile.objects.create(
            user_id=1,
            username='Joe',
            first_name='John',
            surname='Doe',
            email='johndoe@example.com',
            street_address1='123 Noname',
            town_or_city='Nowhere',
            country='Ireland',
        )
        Items.objects.create(
            author_id = 1,
            title = 'Item',
            description = 'Some description',
            views = 0,
            votes = 1,
            category = 'new',
            item_type = 'feature',
        )
        Transaction.objects.create(
            payment_details_id = 1,
            feature_id = 1,
            votes_number = 1,
            total_paid = 5
        )

    def test_profile_name_is_first_name_surname(self):
        transaction = Transaction.objects.get(id=1)
        expected_transaction_name = '{0} {1} paid €{2} for {3}'.format(transaction.payment_details.first_name, transaction.payment_details.surname, transaction.total_paid, transaction.feature.title) 
        self.assertEquals(expected_transaction_name, str(transaction))