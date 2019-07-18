from django.conf.urls import url
from .views import issues

urlpatterns = [
    url(r'', issues, name='issues'),
]