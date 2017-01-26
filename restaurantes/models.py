from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import os




# Create your models here.
class Rest(models.Model):
    nombre = models.CharField(max_length=128)
    cuisine = models.CharField(max_length=20)
    borough = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    building = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)

    
    def __str__(self):
        return self.nombre
