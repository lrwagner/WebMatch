from django.shortcuts import render
from django.views.generic import TemplateView

from app import models
from app.geocoding import get_gps
# Create your views here.

def index_view(request):

    if not models.Person.objects.exists():
           context = {
        'error': 'Error: Databank contains no user'  
        }
    else:
        person = models.Person.objects.all()[0]
        addressGPS = person.street + str(person.house_number) + ',' + person.city + ',' + person.country
        location  = get_gps(address=addressGPS)
        location = str(location)
        context = {
        'person': person, 
        'location': location,
        }

    return render(request, 'app/index.html', context)

class UserCreationView(TemplateView):
    template_name = 'app/usercreation.html'