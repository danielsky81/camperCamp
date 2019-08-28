from django import forms
from .models import Post, PostComment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'tag',)


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ('content',)
