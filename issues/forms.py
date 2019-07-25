from django import forms
from .models import Issue, Comment


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)