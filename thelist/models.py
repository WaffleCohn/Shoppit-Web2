from django.db import models
from django.contrib.auth.models import User

import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=20)
    home_loc = models.CharField(max_length=100)
    rating = models.FloatField(default=2.5)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    name = models.CharField(max_length=100)

class Transaction(models.Model):
    value = models.DecimalField(default=1,max_digits=100,decimal_places=10)
    items = models.ManyToManyField(Item)
    seller = models.ForeignKey(Profile, related_name='+', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, related_name='+', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

# @static_method
def create_profile(username, email, password=None):
    user = User.objects.create_user(username, email, password)
    user.save()

    profile = Profile(user=user)
    profile.save()
    user.save()
    return profile
