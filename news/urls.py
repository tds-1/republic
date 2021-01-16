from django.conf.urls import *
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
]
