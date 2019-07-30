from django.contrib import admin
from .models import Issue, IssuesComment

admin.site.register(Issue)
admin.site.register(IssuesComment)
