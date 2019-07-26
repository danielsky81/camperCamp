from django.contrib import admin
from .models import Issue, CommentIssues

admin.site.register(Issue)
admin.site.register(CommentIssues)
