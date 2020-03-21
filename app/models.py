from django.db import models

class Person(models.Model):
    char_length = 255

    name = models.CharField(max_length= char_length)
    surname = models.CharField(max_length= char_length)
    date_of_birth = models.DateField()

    adress = models.CharField(max_length= char_length)
    house_number = models.PositiveIntegerField()
    zip_code = models.PositiveIntegerField()

    last_access = models.TimeField() # saves as in datetime.date instance



    


# Create your models here.
