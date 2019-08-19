from django.test import TestCase, Client
from django.contrib import auth, messages
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm

class TestViews(TestCase):

    def authenticate(self):
        User.objects.create_user(username='Joe', password='dummypassword')
        return self.client.login(username='Joe', password='dummypassword')

    def test_get_login_page(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')
        
    def test_get_logout_page(self):
        page = self.client.get('/accounts/logout/')
        self.assertRedirects(page, '/accounts/login/?next=/accounts/logout/', 302)

    def test_get_registration_page(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')

    def test_chuj_ci_w_dupe(self):
        auth_user = self.authenticate()
        self.assertTrue(auth_user)
        response = self.client.get('/', follow=True)
        self.assertEqual(str(response.context['user']), 'Joe')
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 302)


