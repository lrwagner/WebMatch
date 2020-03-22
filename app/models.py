from django.db import models
import uuid # import universally unique identifier (ranodm number generation 128 bit)

CHAR_L = 255

class Person(models.Model):
    
    # TODO name/alternativ Username einführen als Primary Key, Form für User Creation, Passwort?
    user_name = models.CharField(verbose_name='User Name', max_length=CHAR_L, primary_key=True, default= uuid4)
    name = models.CharField(verbose_name='First Name', max_length=CHAR_L, default=None)
    surname = models.CharField(verbose_name='Last Name', max_length=CHAR_L, default=None)
    date_of_birth = models.DateField(verbose_name='Date of Birth', default=None)

    # TODO evtl als eigenes Model mit eigener Form, Schritt 2 nach User Creation
    country = models.CharField(max_length=CHAR_L, default=None)
    city = models.CharField(max_length=CHAR_L, default=None)
    street = models.CharField(max_length=CHAR_L, default=None)
    house_number = models.PositiveIntegerField(verbose_name='House Number', default=None)
    zip_code = models.PositiveIntegerField(verbose_name='Zip Code', default=None)
  
     def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        if self.pk is None:
            location = Location()
            location.uuid = self
            location.save()

class Location(models.Model):
    # TODO Foreign Field Verbindung zu Person
    user_name = models.OneToOneField(verbose_name= 'User Name', primary_key=True)
    locationGPS = models.CharField(max_length=CHAR_L, default=None)




class TimeLogs(models.Model):
    last_access = models.TimeField(default=None) # saves as in datetime.date instance
