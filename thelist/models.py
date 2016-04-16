from django.db import models
from django.contrib.auth.models import User

import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=20)
    home_loc = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# @static_method
def create_profile(username, email, password=None):
    user = User.objects.create_user(username, email, password)
    user.save()

    profile = Profile(user=user)
    profile.save()
    user.save()
    return profile
