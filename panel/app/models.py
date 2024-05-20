from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    vivienda = models.TextField(max_length=100)
   # instalacion = models.TextField(max_length=100)
    tipo = models.TextField(max_length=100)
    precio = models.IntegerField(null=False)
    proyeccion = models.IntegerField(null=False)
    consumo = models.IntegerField(null=False)
    panel = models.IntegerField(null=False)
 

