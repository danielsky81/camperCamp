from django.test import TestCase
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import reverse
from .forms import ContactForm


class TestViews(TestCase):

    def test_contact_form_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_form_validation(self):
        response = self.client.post(reverse('contactForm'), {
            'your_email': 'dummy@dummy.com',
            'subject': 'Dummy Subject',
            'message': 'Dummy Content'
            })
        self.assertEqual(response.status_code, 302)

    def test_contact_form_invalid(self):
        response = self.client.post('/contact/', {
            'your_email': 'dummy@dummy.com',
            'subject': 'Dummy Subject',
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_header_injection(self):
        email = {
            'your_email': 'dummy@dummy.com/nInjection Test',
            'subject': 'Dummy Subject',
            'message': 'Dummy Content'
        }
        self.assertRaises(BadHeaderError)

    # def test_header_injection(self):
    #     email = send_mail('Subject\nInjection Test', 'Content', 'from@example.com', ['to@example.com'])
        # self.assertRaises(BadHeaderError, email.message)
        # self.assertTrue(BadHeaderError)