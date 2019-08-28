from django.apps import apps
from django.test import TestCase
from .apps import HelloConfig


class TestHelloConfig(TestCase):

    def test_app(self):
        self.assertEqual('hello', HelloConfig.name)
        self.assertEqual('hello', apps.get_app_config('hello').name)
