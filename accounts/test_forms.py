from django.test import TestCase, Client
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.models import User


class TestUserLoginForm(TestCase):

    def test_login_form_validation(self):
        login_form = UserLoginForm({
            'username': 'Joe',
            'password': 'dummypassword'
        })
        self.assertTrue(login_form.is_valid())

    def test_login_form_failed_validation(self):
        login_form = UserLoginForm({
            'username': 'Joe',
            'password': ''
        })
        self.assertFalse(login_form.is_valid())
        self.assertEqual(login_form.errors['password'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):

    def test_registration_form_validation(self):
        registration_form = UserRegistrationForm({
            'username': 'Joe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'dummypassword',
            'password2': 'dummypassword',
        })
        self.assertTrue(registration_form.is_valid())

    def test_registration_form_failed_validation(self):
        registration_form = UserRegistrationForm({
            'username': 'Joe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'dummypassword1',
            'password2': 'dummypassword2',
        })
        self.assertFalse(registration_form.is_valid())
        self.assertEqual(registration_form.errors['password2'], [u'Passwords does not match. Please try again.'])

    def test_registration_form_email_already_in_database(self):
        data = {
            'username': 'Joe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'dummypassword',
            'password2': 'dummypassword',
        }
        User.objects.create_user(username='Joe1', email=data['email'], password='dummypassword1')
        response = self.client.post('/accounts/register/', data, follow=True)
        self.assertContains(response, u'Looks like the Email address is already in our database. Please login or provide a unique Email address', 1, 200)

    def test_registration_form_password_confirmation_failed(self):
        registration_form = UserRegistrationForm({
            'username': 'Joe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password2': 'dummypassword1',
        })
        self.assertFalse(registration_form.is_valid())
        self.assertEqual(registration_form.errors['password2'], [u'Please confirm your password'])
