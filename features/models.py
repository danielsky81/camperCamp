from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feature(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class CommentFeatures(models.Model):
    
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='comments_feat')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='comments_feat')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.content

class Votes(models.Model):

    vote = models.ForeignKey(Feature, on_delete=models.CASCADE, null=True, blank=False, related_name='add_vote_feat')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='user_feat')

    def __str__(self):
        return self.user