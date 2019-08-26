from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_redirect_when_user_not_authenticated(self):
        user = User.objects.create_user(username='Joe', password='dummypassword')
        self.assertNotIn(user, self.client.session)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)