from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=25)
    contrasena = models.CharField(max_length=10)

    