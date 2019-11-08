from django.db import models
from django.utils import timezone
# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	telefono = models.CharField(max_length=12)
	mensaje = models.TextField()

def __str__(self):
	return self.correo
