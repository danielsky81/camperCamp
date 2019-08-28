from django.conf.urls import url
from .views import contactForm

urlpatterns = [
    url(r'', contactForm, name='contactForm'),
]
