from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
path("",views.Index)
]