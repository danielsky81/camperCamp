from django import forms
from .models import Feature, CommentFeatures


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentFeatures
        fields = ('content',)