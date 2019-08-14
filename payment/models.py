from django.db import models
from items.models import Items
from django.contrib.auth.models import User
from accounts.models import Profile

class Transaction(models.Model):

    payment_details = models.ForeignKey(Profile, null=False)
    feature = models.ForeignKey(Items, null=False)
    votes_number = models.IntegerField(blank=False)
    total_paid = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} {1} paid €{2} for {3}'.format(self.payment_details.first_name, self.payment_details.surname, self.total_paid, self.feature.title)