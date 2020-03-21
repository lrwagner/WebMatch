from django.db import models

CHAR_L = 255

class Person(models.Model):
    

    name = models.CharField(max_length=CHAR_L, default=None)
    surname = models.CharField(max_length=CHAR_L, default=None)
    date_of_birth = models.DateField(default=None)

    country = models.CharField(max_length=CHAR_L, default=None)
    city = models.CharField(max_length=CHAR_L, default=None)
    street = models.CharField(max_length=CHAR_L, default=None)
    house_number = models.PositiveIntegerField(default=None)
    zip_code = models.PositiveIntegerField(default=None)


class Location(models.Model):
    locationGPS = models.CharField(max_length=CHAR_L, default=None)


class TimeLogs(models.Model):
    last_access = models.TimeField(default=None) # saves as in datetime.date instance



    


# Create your models here.
