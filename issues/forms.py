from django import forms
from .models import Issue, IssuesComment


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):

    class Meta:
        model = IssuesComment
        fields = ('content',)