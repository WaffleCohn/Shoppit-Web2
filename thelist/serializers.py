from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Item, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'lat','lon')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name','description','iam_id','owner','lat','lon','quantity')

class TransactionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ('value','items','seller','buyer','datetime')
