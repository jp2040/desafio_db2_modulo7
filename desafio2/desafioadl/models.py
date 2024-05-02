from django.db import models

# Create your models here.
# En desafioadl/models.py
from django.db import models

class Tarea(models.Model):
    descripcion = models.TextField()
    eliminada = models.BooleanField(default=False)

class SubTarea(models.Model):
    descripcion = models.TextField()
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')

