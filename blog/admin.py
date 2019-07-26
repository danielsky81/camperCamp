from django.contrib import admin
from .models import Post, CommentBlog

admin.site.register(Post)
admin.site.register(CommentBlog)