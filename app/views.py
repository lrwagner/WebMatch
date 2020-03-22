from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from app import models
from app import forms
from app.geocoding import get_gps

# Create your views here.

def index_view(request):

    if not User.objects.exists():
           context = {
               'error': 'Error: Databank contains no user'
               }
    else:
        context = {
            'users': User.objects.all()
            }

    return render(request, 'app/index.html', context)

def adress_signup_view(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():

        data = form.cleaned_data
        address = data['street'] + str(data['house_number']) + ',' + data['city'] + ',' + data['country']
        # TODO save gps in Location via Foreignkey
        # gps = get_gps(address)
        form.save()
        form = PersonForm()
    
    context = {
        'form': form,
        }
    return render(request, 'app/usercreation.html', context)

def user_signup_view(request):
    form = forms.UserSignupForm(request.POST or None)

    if form.is_valid():

        form.save()
        form = forms.UserSignupForm()
    
    context = {
        'form': form
    }
    return render(request, 'app/user_signup.html', context)