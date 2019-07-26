from django import forms
from .models import Issue, CommentIssues


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentIssues
        fields = ('content',)