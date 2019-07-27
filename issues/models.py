from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Issue(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    user_votes = models.IntegerField(default=0)
    CATEGORIES = [('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')]
    category = models.CharField(max_length=12, choices=CATEGORIES, default='to do')

    def __str__(self):
        return self.title

class CommentIssues(models.Model):
    
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments_issue')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.content

class Votes(models.Model):

    vote_issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.user