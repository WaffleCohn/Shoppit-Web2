from django.contrib import admin

# Register your models here.
from .models import Item, Profile, Transaction
admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(Transaction)
