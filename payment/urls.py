from django.conf.urls import url
from .views import checkout, adding_vote, removing_vote, cancel_vote, payment

urlpatterns = [
    url(r'(?P<pk>\d+)/checkout/$', checkout, name='checkout'),
    url(r'^(?P<pk>\d+)/checkout/adding_vote/$', adding_vote, name='adding_vote'),
    url(r'^(?P<pk>\d+)/checkout/removing_vote/$', removing_vote, name='removing_vote'),
    url(r'^(?P<pk>\d+)/checkout/cancel_vote/$', cancel_vote, name='cancel_vote'),
    url(r'(?P<pk>\d+)/payment/$', payment, name='payment'),
]
