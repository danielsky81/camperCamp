from django.test import TestCase
from .forms import ContactForm
from django.core.mail import send_mail


class TestViews(TestCase):

    def test_contact_form_validation(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        # form_data = {
        #     'your_email': 'dummy@dummy.com',
        #     'subject': 'Dummy Subject',
        #     'message': 'Dummy Content'
        # }
        # form = ContactForm(form_data)
        # self.assertTrue(form.is_valid())
        # subject = form.cleaned_data['subject'] 
        # your_email = form.cleaned_data['your_email'] 
        # message = form.cleaned_data['message']
        # send_mail(subject, message + ' | Email sent from: ' + your_email, your_email, ['djangoprojectci@gmail.com'])
        # self.assertEqual(send_mail, 'Dummy Subject, Dummy Content | Email sent from: dummy@dummy.com, djangoprojectci@gmail.com')
        # response = self.client.get('/', form, follow=True)
        # self.assertContains(response, 'Thank you for your message!', 1, 200)