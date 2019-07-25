from django.conf.urls import url
from .views import get_issues, issue_detail, create_or_edit_issue, add_comment_to_issue, edit_comment, delete_comment

urlpatterns = [
    url(r'^$', get_issues, name='get_issues'),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^new/$', create_or_edit_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_issue, name='edit_issue'),
    url(r'^(?P<pk>\d+)/comment/', add_comment_to_issue, name='add_comment_to_issue'),
    url(r'^comment/(?P<pk>\d+)/edit/', edit_comment, name='edit_comment'),
    url(r'^comment/(?P<pk>\d+)/delete/', delete_comment, name='delete_comment'),
]