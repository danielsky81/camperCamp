from django.conf.urls import url, include
from .views import login, logout, registration, update_profile
from accounts import url_reset

urlpatterns = [
    url(r'login/', login, name='login'),
    url(r'logout/', logout, name='logout'),
    url(r'register/', registration, name='registration'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^(?P<pk>\d+)/update-profile/', update_profile, name='update_profile'),
]