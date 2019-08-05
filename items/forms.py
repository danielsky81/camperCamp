from django import forms
from .models import Items, ItemComments


class ItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):

    class Meta:
        model = ItemComments
        fields = ('content',)