from django.test import TestCase
from .models import Profile


class ProfileModelTest(TestCase):

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

    def test_profile_name_is_first_name_surname(self):
        user = Profile.objects.get(id=1)
        expected_profile_name = '{0} {1}'.format(user.first_name, user.surname)
        self.assertEquals(expected_profile_name, str(user))
