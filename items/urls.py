from django.conf.urls import url
from .views import get_items, item_detail, create_or_edit_item, add_comment_to_item, edit_comment_item, delete_comment_item, add_vote, admin_update

urlpatterns = [
    url(r'^issues/$', get_items, name='get_issues'),
    url(r'^features/$', get_items, name='get_features'),
    url(r'^(?P<pk>\d+)/$', item_detail, name='item_detail'),
    url(r'^issues/new/$', create_or_edit_item, name='new_issue'),
    url(r'^features/new/$', create_or_edit_item, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_item, name='edit_item'),
    url(r'^(?P<pk>\d+)/category_update/$', admin_update, name='admin_update'),
    url(r'^(?P<pk>\d+)/comment/$', add_comment_to_item, name='add_comment_to_item'),
    url(r'^(?P<pk>\d+)/vote/$', add_vote, name='add_vote'),
    url(r'^comment/(?P<pk>\d+)/edit/$', edit_comment_item, name='edit_comment_item'),
    url(r'^comment/(?P<pk>\d+)/delete/$', delete_comment_item, name='delete_comment_item'),
]