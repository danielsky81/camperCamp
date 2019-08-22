from django.test import TestCase
from django.contrib.auth.models import User
from .backends import EmailAuth


class TestBackendAuth(TestCase):

    def test_username_valid_authentication(self):
        User.objects.create_user(username='Joe', email='johndoe@example.com', password='dummypassword')
        user = EmailAuth.authenticate(self, username='Joe', password='dummypassword')
        self.assertEqual(user.username, 'Joe')
        self.assertEqual(user.email, 'johndoe@example.com')

    def test_not_valid_username_authentication(self):
        EmailAuth.authenticate(self, username='Joe', password='dummypassword')
        self.failureException(User.DoesNotExist)

    def test_email_authentication_wrong_password(self):
        User.objects.create_user(username='Joe', email='johndoe@example.com', password='dummypassword')
        user = EmailAuth.authenticate(self, username='Joe', password='differentpassword')
        self.assertIsNone(user)

    def test_get_user_validation(self):
        user = User.objects.create_user(username='Joe', email='johndoe@example.com', password='dummypassword')
        get_user = EmailAuth.get_user(self, user.id)
        self.assertEqual(get_user.username, 'Joe')
        self.assertEqual(get_user.email, 'johndoe@example.com')

    def test_get_user_not_active(self):
        user = User.objects.create_user(username='Joe', email='johndoe@example.com', password='dummypassword', is_active=False)
        get_user = EmailAuth.get_user(self, user.id)
        self.assertIsNone(get_user)

    def test_get_user_which_does_not_exist(self):
        EmailAuth.get_user(self, 2)
        self.failureException(User.DoesNotExist)
