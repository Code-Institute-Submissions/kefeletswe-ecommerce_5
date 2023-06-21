# using this as a shell coppied from online_shop url
from django.contrib import admin
from django.urls import path # no need for include here
from . import views

urlpatterns = [
    path('', views.index, name='myapp')


]


