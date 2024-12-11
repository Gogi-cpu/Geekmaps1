
# Create your models here.
from django.db import models
import datetime
import os

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Objeto(models.Model):
    id          = models.CharField(primary_key=True,max_length=10)
    nombre      = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    disponibles = models.CharField(max_length=20)
    ubicacion   = models.CharField(max_length=20)

class Usuario(models.Model):
    correo      = models.CharField(primary_key=True, max_length=50)
    username    = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)    
    tipo        = models.CharField(max_length=50)   
    
    def __str__(self):
        return str(self.username)+" "+str(self.password) + "   "+ self.correo +" "+str(self.password) 

class Fotos(models.Model):
    id_img      = models.CharField(primary_key=True,max_length=10)
    nombre      = models.CharField(max_length=20)
    imagen      = models.ImageField(upload_to=filepath, null=True, blank=True)