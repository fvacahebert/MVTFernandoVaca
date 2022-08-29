from django.db import models

# Create your models here.

class Familia(models.Model):
    DNI=models.IntegerField()
    nombre=models.CharField(max_length=30)
    parentezco=models.CharField(max_length=30)
    fecha_de_cumpleaños=models.DateField()



