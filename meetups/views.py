from ast import Try
from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup

# Create your views here.
def Index(request):
    meetups = Meetup.objects.all()
    return render(request,"meetups/index.html",{
        'meetups':meetups
        })


def meetup_details (request,meetup_slug) :
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render ( request , 'meetups/meetup-detail.html' , {
            'meetup_found' : True ,
            'meetup_title' : selected_meetup.title,
            'meetup_description' : selected_meetup.description,
            'meetup_img': selected_meetup.image.url,
            'meetup_city': selected_meetup.location.name,
            'meetup_addr': selected_meetup.location.address,

         })
    except Exception as exe:
        return render ( request , 'meetups/meetup-detail.html' , {
            'meetup_found' : False ,
         })