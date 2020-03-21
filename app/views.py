from django.shortcuts import render
from django.views.generic import ListView

from app import models

# Create your views here.
class IndexView(ListView):
    template_name = 'app/index.html'

    def get_queryset(self):
        object_list = models.Person.objects.all()
        return object_list

    
    