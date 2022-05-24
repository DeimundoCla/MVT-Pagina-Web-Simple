from django.db import models

# Create your models here.


class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    fecha = models.DateField()
    ciudad = models.CharField(max_length=40)
    email = models.EmailField()