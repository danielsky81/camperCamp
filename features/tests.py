from django.test import TestCase
from .models import Feature

class FeatureTests(TestCase):

    def test_str(self):
        test_title = Feature(title='A Feature')
        self.assertEqual(str(test_title), 'A Feature')
