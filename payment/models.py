from django.db import models
from items.models import Votes

class Payment(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class PaymentDetails(models.Model):
    payment = models.ForeignKey(Payment, null=False)
    feature_vote = models.ForeignKey(Votes, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)