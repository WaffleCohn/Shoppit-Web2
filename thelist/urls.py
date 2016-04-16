from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'user', views.view_user),
]
