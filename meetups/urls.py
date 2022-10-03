from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
path("meetups/",views.Index),
path("meetups/<slug:meetup_slug>/",views.meetup_details,name='meetup_detail')
]