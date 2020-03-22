from django.db import models
from django.conf import settings

CHAR_L = 255

class Adress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # this is the connection to primary key User
    # TODO evtl als eigenes Model mit eigener Form, Schritt 2 nach User Creation
    country = models.CharField(max_length=CHAR_L, default=None)
    city = models.CharField(max_length=CHAR_L, default=None)
    street = models.CharField(max_length=CHAR_L, default=None)
    house_number = models.PositiveIntegerField(verbose_name='House Number', default=None)
    zip_code = models.PositiveIntegerField(verbose_name='Zip Code', default=None)
    locationGPS = models.CharField(max_length=CHAR_L, default=None)

class TimeLogs(models.Model):
    last_access = models.TimeField(default=None) # saves as in datetime.date instance
