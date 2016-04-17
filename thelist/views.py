from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max, Avg, Min
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

import numpy as np

from .models import *
from .serializers import *

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@api_view(['GET'])
def get_user(request, username):
    if request.method == "GET":
        profile = User.objects.get(username=username).profile
        serializer = ProfileSerializer(profile)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def get_items_all(request):
    if request.method == "GET":
        serializer = ItemSerializer(Item.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_item_id(request, id):
    if request.method == "GET":
        item = Item.objects.get(id=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

# untested
@api_view(['GET'])
def get_items_owner(request, username):
    if request.method == "GET":
        profile = User.objects.get(username=username).profile
        items = Item.objects.get(owner=profile)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_transactions_all(request):
    if request.method == "GET":
        serializer = TransactionSerializer(Transaction.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_transaction_id(request, id):
    if request.method == "GET":
        transaction = Transaction.objects.get(id=id)
        serializer = TransactionSerializer(item)
        return Response(serializer.data)

# untested
@api_view(['GET'])
def get_transactions_owner(request, username):
    if request.method == "GET":
        profile = User.objects.get(username=username).profile
        transactions = Transaction.objects.get(owner=profile)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

# calculate distance from 'x' to a list of points
# from: https://stackoverflow.com/a/6659808
def distance(x,y):
    earth_radius_miles = 3956.0
    dlat = np.radians(y[:,0]) - np.radians(x[0])
    dlon = np.radians(y[:,1]) - np.radians(x[1])
    a = np.square(np.sin(dlat/2.0)) + np.cos(np.radians(x[0])) * np.cos(np.radians(y[:,0])) * np.square(np.sin(dlon/2.0))
    great_circle_distance = 2 * np.arcsin(np.minimum(np.sqrt(a), np.repeat(1, len(a))))
    d = earth_radius_miles * great_circle_distance
    return d

def get_closest(lat,lon):
    profs = Profile.objects.all()
    y = np.array(list(map(lambda x: [x.lat, x.lon, x.id], profs)))
    d = distance([lat,lon], y[:,[0,1]])
    d = np.hstack((y,d[np.newaxis,:].T))
    d = d[d[:,-1].argsort()] # sort based on distance

    # get the id of the closest person
    p_id = int(d[0,2])
    p = Profile.objects.get(id=p_id)

    return p
