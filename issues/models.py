from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Issue(models.Model):

    CATEGORIES = [
        ('new', 'new'),
        ('to do', 'to do'),
        ('in progress', 'in progress'),
        ('done', 'done'),
        ('rejected', 'rejected'),
        ('require data', 'require data'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='issues')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    category = models.CharField(max_length=12, choices=CATEGORIES, default='new')

    def __str__(self):
        return self.title

class IssuesComment(models.Model):
    
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='issue_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='issue_user_comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return 'Comment on %s by %s' % (self.issue.title, self.author.username)

class Votes(models.Model):

    issue_id = models.OneToOneField(Issue, on_delete=models.CASCADE, related_name='vote')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='issue_votes')

    def __str__(self):
        return self.user