from ast import Try
from atexit import register
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.
def Index(request):
    meetups = Meetup.objects.all()
    return render(request,"meetups/index.html",{
        'meetups':meetups
        })


def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('registered_success',meetup_slug=meetup_slug)

        return render (request , 'meetups/meetup-detail.html' , {
            'meetup_found' : True ,
            'meetups' : selected_meetup,
            'form' : registration_form
         })
    except Exception as exe:
        print(exe)
        return render (request , 'meetups/meetup-detail.html' , {
            'meetup_found' : False ,
         })

def meetup_added(request,meetup_slug):
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html',{
            'meetups' : selected_meetup,
         })