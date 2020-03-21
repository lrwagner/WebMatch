from django.db import models

class Person(models.Model):
    char_length = 255

    name = models.CharField(max_length=char_length, default=None)
    surname = models.CharField(max_length=char_length, default=None)
    date_of_birth = models.DateField(default=None)

    adress = models.CharField(max_length=char_length, default=None)
    house_number = models.PositiveIntegerField(default=None)
    zip_code = models.PositiveIntegerField(default=None)

    last_access = models.TimeField(default=None) # saves as in datetime.date instance



    


# Create your models here.
