from django.test import TestCase
from .models import Transaction
from items.models import Items, Votes
from accounts.models import Profile
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Joe',
            password='dummypassword'
        )
        self.client.login(username='Joe', password='dummypassword')
        feature = Items.objects.create(
            author_id = 1,
            title = 'feature',
            description = 'Some description',
            views = 0,
            votes = 0,
            category = 'new',
            item_type = 'feature',
        )
        session = self.client.session
        session['feature'] = 1
        session['votes_number'] = 1
        session.save()

    def test_checkout_view(self):
        item = get_object_or_404(Items, pk=1) 
        votes_number = self.client.session.get('votes_number', 'votes_number')
        response = self.client.get('/items/1/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_adding_vote(self):
        item = get_object_or_404(Items, pk=1)
        votes_number = self.client.session.get('votes_number', 'votes_number')
        self.assertEqual(votes_number, 1)
        if votes_number > 0:
            votes_number += 1
        self.assertEqual(votes_number, 2)
        session = self.client.session
        session['votes_number'] = votes_number
        session.save()
        response = self.client.post(reverse('adding_vote', kwargs={'pk': '1'}), {
            'votes_number': 'votes_number'
        })
        self.assertRedirects(response, '/items/1/checkout/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_removing_vote(self):
        item = get_object_or_404(Items, pk=1) 
        session = self.client.session
        session['votes_number'] = 2
        session.save()
        votes_number = self.client.session.get('votes_number', 'votes_number')
        self.assertEqual(votes_number, 2)
        if votes_number > 1:
            votes_number -= 1
        self.assertEqual(votes_number, 1)
        session = self.client.session
        session['votes_number'] = votes_number
        session.save()
        response = self.client.post(reverse('removing_vote', kwargs={'pk': '1'}), {
            'votes_number': 'votes_number'
        })
        self.assertRedirects(response, '/items/1/checkout/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_cancel_voting(self):
        item = get_object_or_404(Items, pk=1)
        response = self.client.post(reverse('cancel_vote', kwargs={'pk': '1'}), {
            'votes_number': 'votes_number'
        })
        self.assertRedirects(response, '/items/1/', status_code=302, target_status_code=200, fetch_redirect_response=True)


class TestPayment(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Joe',
            password='dummypassword'
        )
        self.client.login(username='Joe', password='dummypassword')
        feature = Items.objects.create(
            author_id = 1,
            title = 'feature',
            description = 'Some description',
            views = 0,
            votes = 0,
            category = 'new',
            item_type = 'feature',
        )
        profile = Profile.objects.create(
            user_id=1,
            username='Joe',
            first_name='John',
            surname='Doe'
        )
        session = self.client.session
        session['feature'] = 1
        session['votes_number'] = 1
        session['total'] = 5
        session.save()

    def test_get_payment_view(self):
        response = self.client.get('/items/1/payment/')
        self.assertEqual(response.status_code, 200)

    def test_payment_order_form(self):
        response = self.client.post(reverse('payment', kwargs={'pk': '1'}), {
            'first_name': 'Joe',
            'surname': 'Doe',
            'street_address1': 'Dummy street',
            'street_address2': '123',
            'town_or_city': 'Dublin',
            'country': 'Ireland'
        }) 
        self.assertEqual(response.status_code, 200)
        
    def test_payment_order_payment_form(self):
        response = self.client.post(reverse('payment', kwargs={'pk': '1'}), {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2020',
        }) 
        self.assertEqual(response.status_code, 200)

    def test_transaction_payment(self):
        item = get_object_or_404(Items, pk=1)
        profile = get_object_or_404(Profile, username='Joe') 
        votes_number = self.client.session.get('votes_number', 'votes_number') 
        total = self.client.session.get('total', 'total')
        user_details = get_object_or_404(Profile, pk=1)
        transaction = Transaction(payment_details = user_details, feature = item, votes_number = votes_number, total_paid = total) 
        transaction.save() 
        response = self.client.post(reverse('payment', kwargs={'pk': '1'}), {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2020',
        })
        self.assertEqual(response.status_code, 200)
        votes = Votes.objects.filter(voted_item=item) 
        user = User.objects.get(username='Joe')
        upvoted = False
        vote = Votes(voted_date=timezone.now(), user = user, voted_item = item) 
        vote.votes_number = vote.votes_number + votes_number 
        vote.save() 
        item.votes = item.votes + votes_number 
        item.save() 
        response = self.client.post(reverse('item_detail', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)
        


    # def test_payment_transaction(self):
    #     item = get_object_or_404(Items, pk=1) 
    #     profile = get_object_or_404(Profile, username='Joe') 
    #     votes_number = self.client.session.get('votes_number', 'votes_number')
    #     total = self.client.session.get('total', 'total')
    #     order_form = ({
    #         'first_name': 'Joe',
    #         'surname': 'Doe',
    #         'street_address1': 'Dummy street',
    #         'street_address2': '123',
    #         'town_or_city': 'Dublin',
    #         'country': 'Ireland'
    #     })
    #     response = self.client.post(reverse('payment', kwargs={'pk': '1'}), order_form)
    #     self.assertEqual(response.status_code, 200)
    #     # user_details = order_form.save(commit=False) 
    #     # user_details.updated_date = timezone.now() 
    #     # user_details.save()
    #     transaction = Transaction(payment_details = profile, feature = item, votes_number = votes_number, total_paid = total) 
    #     transaction.save()
    #     response = self.client.post('/items/1/payment/', {
    #         'credit_card_number': '4242424242424242',
    #         'cvv': '100',
    #         'expiry_month': '6',
    #         'expiry_year': '2020',
    #         }, follow=True)

    # def test_card_accepted(self):
    #     response = self.client.post('/items/1/payment/', {
    #         'credit_card_number': '4242424242424242',
    #         'cvv': '100',
    #         'expiry_month': '6',
    #         'expiry_year': '2019',
    #         }, follow=True)
    #     response = self.client.get(reverse('item_detail', kwargs={'pk': '1'}))
    #     self.assertContains(response, 'You have successfully paid! Thanks for voting!', status_code=200)
        


    # def test_blog_form_validation(self):
    #     form = MakePaymentForm({
    #         'credit_card_number': '4242424242424242',
    #         'cvv': '123',
    #         'expiry_month': '1',
    #         'expiry_year': '2021',
    #         'stripe_id': '1',
    #     })
    #     response = self.client.post(reverse('payment', kwargs={'pk': '1'}))
    #     self.assertEqual(response.status_code, 200)

    # def test_trans(self):
    #     order_form = OrderForm({
    #         'first_name': 'Joe',
    #         'surname': 'Doe',
    #         'street_address1': 'Dummy street',
    #         'street_address2': '123',
    #         'town_or_city': 'Dublin',
    #         'country': 'Ireland'
    #     })
    #     user_details = order_form.save(commit=False) 
    #     user_details.updated_date = timezone.now() 
    #     user_details.save() 
    #     item = get_object_or_404(Items, pk=1)
    #     votes_number = self.client.session.get('votes_number', 'votes_number') 
    #     total = self.client.session.get('total', 'total') 
    #     transaction = Transaction(
    #         payment_details = user_details,
    #         feature = item,
    #         votes_number = votes_number,
    #         total_paid = total
    #     ) 
    #     transaction.save() 
    #     response = self.client.post(reverse('payment', kwargs={'pk': '1'}), follow=True)
    #     self.assertEqual(response.status_code, 200) 

    # def test_adding_votes_on_successfull_payment(self):
    #     item = get_object_or_404(Items, pk=1) 
    #     votes = Votes.objects.filter(voted_item=item) 
    #     user = User.objects.get(username='Joe')
    #     vote = Votes(voted_date=timezone.now(), user = user, voted_item = item)
    #     votes_number = self.client.session.get('votes_number', 'votes_number') 
    #     vote.votes_number = vote.votes_number + votes_number 
    #     vote.save() 
    #     item.votes = item.votes + votes_number 
    #     item.save()
    #     response = self.client.post(reverse('payment', kwargs={'pk': '1'}), follow=True)
    #     self.assertEqual(response.status_code, 200) 