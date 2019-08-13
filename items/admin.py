from django.contrib import admin
from .models import Items, ItemComments, Votes

admin.site.register(Items)
admin.site.register(ItemComments)
admin.site.register(Votes)
