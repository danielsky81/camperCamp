from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Feature(models.Model):

    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

