from django.db import models
from items.models import Items
from django.contrib.auth.models import User

class Payment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='feature')
    first_name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Payment id: {0} on {1} by {2} {3}'.format(self.id, self.date, self.first_name, self.surname)


class Transaction(models.Model):

    payment_details = models.ForeignKey(Payment, null=False)
    feature = models.ForeignKey(Items, null=False)
    votes_number = models.IntegerField(blank=False)
    total_paid = models.IntegerField(blank=False)

    def __str__(self):
        return '{0} {1} paid €{2} for {3}'.format(self.payment_details.first_name, self.payment_details.surname, self.total_paid, self.feature.title)