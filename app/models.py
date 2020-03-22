from django.db import models

CHAR_L = 255

class Person(models.Model):
    
    # TODO name als Primary Key, Form für User Creation, Passwort?
    name = models.CharField(max_length=CHAR_L, default=None)
    surname = models.CharField(max_length=CHAR_L, default=None)
    date_of_birth = models.DateField(default=None)

    # TODO evtl als eigenes Model mit eigener Form, Schritt 2 nach User Creation
    country = models.CharField(max_length=CHAR_L, default=None)
    city = models.CharField(max_length=CHAR_L, default=None)
    street = models.CharField(max_length=CHAR_L, default=None)
    house_number = models.PositiveIntegerField(default=None)
    zip_code = models.PositiveIntegerField(default=None)


class Location(models.Model):
    # TODO Foreign Field Verbindung zu Person
    locationGPS = models.CharField(max_length=CHAR_L, default=None)


class TimeLogs(models.Model):
    last_access = models.TimeField(default=None) # saves as in datetime.date instance
