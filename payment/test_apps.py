from django.apps import apps
from django.test import TestCase
from .apps import PaymentConfig


class TestPaymentConfig(TestCase):

    def test_app(self):
        self.assertEqual('payment', PaymentConfig.name)
        self.assertEqual('payment', apps.get_app_config('payment').name)