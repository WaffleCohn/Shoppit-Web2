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

from .models import *

def view_user(request):
    username = request.GET.get("username")
    profile = User.objects.get(username=username).profile
    return HttpResponse(profile.user.username)
