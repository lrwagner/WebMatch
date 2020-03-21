from django import forms

from .models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'date_of_birth',
            'country',
            'city',
            'street',
            'house_number',
            'zip_code'
        ]
