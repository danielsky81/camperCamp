from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Items(models.Model):

    CATEGORIES = [
        ('new', 'new'),
        ('to do', 'to do'),
        ('in progress', 'in progress'),
        ('done', 'done'),
        ('rejected', 'rejected'),
        ('require data', 'require data'),
    ]

    TYPES = [
        ('issue', 'issue'),
        ('feature', 'feature'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='items')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
    category_update = models.DateTimeField(null=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    category = models.CharField(max_length=12, choices=CATEGORIES, default='new')
    item_type = models.CharField(max_length=7, choices=TYPES, blank=False, null=False)

    def __str__(self):
        return '%s titled: %s' % (self.item_type, self.title)

class ItemComments(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='item_user_comments')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='item_comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return 'Comment on %s by %s' % (self.item.title, self.author.username)

class Votes(models.Model):

    voted_item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=False, related_name='vote')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='item_votes')
    voted_date = models.DateTimeField(auto_now_add=True)
    votes_number = models.IntegerField(default=0)

    def __str__(self):
        return self.user