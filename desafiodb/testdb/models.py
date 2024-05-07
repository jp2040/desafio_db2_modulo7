from django.db import models

# Create your models here.
class adltest(models.Model):
    campo1 = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
   

