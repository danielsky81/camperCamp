from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post, delete_post, add_comment_to_post, edit_comment_post, delete_comment_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name='delete_post'),
    url(r'^(?P<pk>\d+)/comment/', add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/edit/', edit_comment_post, name='edit_comment_post'),
    url(r'^comment/(?P<pk>\d+)/delete/', delete_comment_post, name='delete_comment_post'),
]