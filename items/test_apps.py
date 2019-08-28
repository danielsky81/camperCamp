from django.apps import apps
from django.test import TestCase
from .apps import IssuesConfig


class TestIssuesConfig(TestCase):

    def test_app(self):
        self.assertEqual('items', IssuesConfig.name)
        self.assertEqual('items', apps.get_app_config('items').name)
