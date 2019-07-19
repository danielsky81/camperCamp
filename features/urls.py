from django.conf.urls import url
from .views import get_features, feature_detail, create_or_edit_feature

urlpatterns = [
    url(r'^$', get_features, name='get_features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^new/$', create_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feature, name='edit_feature')
]