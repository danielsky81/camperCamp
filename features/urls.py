from django.conf.urls import url
from .views import get_features, feature_detail, create_or_edit_feature, add_comment_to_feature, edit_comment, delete_comment

urlpatterns = [
    url(r'^$', get_features, name='get_features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^new/$', create_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feature, name='edit_feature'),
    url(r'^(?P<pk>\d+)/comment/', add_comment_to_feature, name='add_comment_to_feature'),
    url(r'^comment/(?P<pk>\d+)/edit/', edit_comment, name='edit_comment'),
    url(r'^comment/(?P<pk>\d+)/delete/', delete_comment, name='delete_comment'),
]