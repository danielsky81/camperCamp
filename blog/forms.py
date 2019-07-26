from django import forms
from .models import Post, CommentBlog


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentBlog
        fields = ('content',)