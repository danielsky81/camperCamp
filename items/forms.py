from django import forms
from .models import Items, ItemComments


class ItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('item_type', 'title', 'description')

class CommentForm(forms.ModelForm):

    class Meta:
        model = ItemComments
        fields = ('content',)