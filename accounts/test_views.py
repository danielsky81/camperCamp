from django.test import TestCase, Client
from django.contrib import auth, messages
from django.shortcuts import get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.utils import timezone 

class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='Joe', password='dummypassword')
        profile = Profile.objects.create(user_id=1, username='Joe', first_name='John', surname='Doe')
        user.save()
        profile.save()
    
    # Login

    def test_get_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_authenticated_user_redirected_from_login_page(self):
        self.client.login(username='Joe', password='dummypassword')
        response = self.client.get('/accounts/login/')
        self.assertRedirects(response, '/dashboard/', 302)

    def test_valid_user_login(self):
        response = self.client.post('/accounts/login/', {
            'username': 'Joe',
            'password': 'dummypassword'
        }, follow=True)
        self.assertContains(response, 'You have successfully logged in! Enjoy!', 1, 200)

    def test_invalid_user_login(self):
        response = self.client.post('/accounts/login/', {
            'username': 'Joe',
            'password': 'wrong_password'
        }, follow=True)
        self.assertContains(response, 'Your username or password is incorrect. Please try again.', 1, 200)

    # Logout

    def test_get_logout_page(self):
        self.client.login(username='Joe', password='dummypassword')
        response = self.client.get('/accounts/logout/')
        self.assertRedirects(response, '/', 302)

    # Registration

    def test_get_registration_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_authenticated_user_redirected_from_registration_page(self):
        self.client.login(username='Joe', password='dummypassword')
        response = self.client.get('/accounts/register/')
        self.assertRedirects(response, '/dashboard/', 302)

    def test_valid_user_registration(self):
        new_user = {
            'username': 'Ed',
            'first_name': 'Eddie',
            'last_name': 'Ed',
            'email': 'ededdie@example.com',
            'password1': 'password',
            'password2': 'password',
        }
        response = self.client.post('/accounts/register/', new_user, follow=True)
        self.assertContains(response, 'You have successfully registered', 1, 200)

    # Update profile

    def test_update_user_profile_page(self):
        self.client.login(username='Joe', password='dummypassword')
        response = self.client.post(reverse('update_profile', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_valid_update_user_profile(self):
        self.client.login(username='Joe', password='dummypassword')
        profile = get_object_or_404(Profile, pk=1)
        self.assertNotEqual(profile.email, 'johndoe@example.com')
        response = self.client.get(reverse('update_profile', kwargs={'pk': '1'}))
        profile.email = 'johndoe@example.com'
        profile.street_address1 = '123 Noname'
        profile.town_or_city = 'Nowhere'
        profile.country = 'Ireland'
        profile.updated_date = timezone.now()
        profile.save()
        self.assertEqual(profile.email, 'johndoe@example.com')
        self.assertEqual(response.status_code, 200)

    # Delete profile

    def test_delete_user_profile(self):
        self.client.login(username='Joe', password='dummypassword')
        profile = get_object_or_404(Profile, pk=1)
        self.assertEqual(Profile.objects.count(), 1)
        response = self.client.get(reverse('delete_profile', kwargs={'pk': '1'}))
        profile.delete()
        self.assertEqual(Profile.objects.count(), 0)
        self.assertRedirects(response, '/', 302)