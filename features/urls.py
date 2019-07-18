from django.conf.urls import url
from .views import features

urlpatterns = [
    url(r'', features, name='features'),
]