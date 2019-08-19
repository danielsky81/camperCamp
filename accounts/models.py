from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=150, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
    image = models.ImageField(default='default_profile_img.jpg', upload_to='img')


    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.surname)
