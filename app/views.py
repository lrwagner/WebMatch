from django.shortcuts import render
from django.views.generic import TemplateView

from app import models
from app.geocoding import get_gps
from .forms import PersonForm, UserSignupForm
# Create your views here.

def index_view(request):

    if not models.Person.objects.exists():
           context = {
               'error': 'Error: Databank contains no user'
               }
    else:
        persons = models.Person.objects.all()
        context = {
            'persons': persons
            }

    return render(request, 'app/index.html', context)

def user_creation_view(request):
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
    form = UserSignupForm(request.POST or None)

    if form.is_valid():

        form.save()
        form = UserSignupForm()
    
    context = {
        'form': form
    }
    return render(request, 'app/user_signup.html', context)