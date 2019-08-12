from django.conf.urls import url
from .views import hello, get_data

urlpatterns = [
    url(r'^get_data/', get_data, name='get_data'),
    url(r'hello/$', hello, name='hello'),
]