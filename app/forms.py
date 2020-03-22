from django import forms

from .models import Person

class PersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove colon as label prefix in .html
        self.label_suffix = ""

    class Meta:
        model = Person
        fields = '__all__'
