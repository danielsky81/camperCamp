from django.conf.urls import url
from .views import get_issues, issue_detail, create_or_edit_issue, add_comment_to_issue, edit_comment_issue, delete_comment_issue, add_vote

urlpatterns = [
    url(r'^$', get_issues, name='get_issues'),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^new/$', create_or_edit_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_issue, name='edit_issue'),
    
    url(r'^(?P<pk>\d+)/comment/$', add_comment_to_issue, name='add_comment_to_issue'),
    url(r'^(?P<pk>\d+)/vote/$', add_vote, name='add_vote'),
    url(r'^comment/(?P<pk>\d+)/edit/$', edit_comment_issue, name='edit_comment_issue'),
    url(r'^comment/(?P<pk>\d+)/delete/$', delete_comment_issue, name='delete_comment_issue'),
]