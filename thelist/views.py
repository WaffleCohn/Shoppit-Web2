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

from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, list_route
from rest_framework.response import Response

import numpy as np

import urllib, simplejson

from .models import *
from .serializers import *

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # lookup_field = 'id'

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # @list_route()
    # def by_owner(self,request,username):
        # profile = User.objects.get(username).profile
        # print(profile)
        # items = Item.objects.filter(owner=profile)
        # serializer = ItemSerializer(items, many=True)
        # return Response(serializer.data)

class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ItemList(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        profile = User.objects.get(username=self.kwargs['username']).profile
        # print(profile)
        return Item.objects.filter(owner=profile)

class TransactionList(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        profile = User.objects.get(username=self.kwargs['username']).profile
        # print(profile)
        return Transaction.objects.filter(owner=profile)

# untested
@api_view(['POST'])
def register_account(request):
    username = request.POST.get('username','')
    email = request.POST.get('email','')
    password = request.POST.get('password',None)
    create_profile(username, email, password=password)

# untested
@api_view(['GET'])
def nearest_items(request,lat,lon):
    return HttpResponse(items_in_radius([lat,lon]))

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

def items_in_radius(latlon,radius):
    items = Item.objects.all()
    y = np.array(list(map(lambda x: [x.lat, x.lon, x.id], items)))
    d = distance(latlon, y[:,[0,1]])
    d = np.hstack((y,d[np.newaxis,:].T))
    d = d[d[:,-1] <= radius] # threshold the distance
    d = d[d[:,-1].argsort()] # sort based on distance
    d = d[:,[-2,-1]]

    d = d.tolist()
    d = map(lambda x: (Item.objects.get(id=x[0]),x[1]), d)

    return d

def get_closest(latlon):
    profs = Profile.objects.all()
    y = np.array(list(map(lambda x: [x.lat, x.lon, x.id], profs)))
    d = distance(latlon, y[:,[0,1]])
    d = np.hstack((y,d[np.newaxis,:].T))
    d = d[d[:,-1].argsort()] # sort based on distance

    # get the id of the closest person
    p_id = int(d[0,2])
    p = Profile.objects.get(id=p_id)

    return p

def address_to_gps(query, from_sensor=False):
    query = query.encode('utf-8')
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urllib.urlencode(params)
    json_response = urllib.urlopen(url)
    response = simplejson.loads(json_response.read())
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
    else:
        latitude, longitude = None, None
    return latitude, longitude
