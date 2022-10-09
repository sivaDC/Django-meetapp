from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
path("",views.Index,name="meetup"),
path("meetups/<slug:meetup_slug>/success/",views.meetup_added,name='registered_success'),
path("meetups/<slug:meetup_slug>/",views.meetup_details,name='meetup_detail'),
]