from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    TAGS = [
        ('issue', 'issue'),
        ('feature', 'feature'),
        ('news', 'news'),
        ('other', 'other'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='posts')
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, null=False, blank=False, choices=TAGS, default='news')
    updated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PostComment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='post_comments')
    content = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return 'Comment on %s by %s' % (self.post.title, self.author.username)
