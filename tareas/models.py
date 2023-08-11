from django.db import models

# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    #to show data in the admin site
    def __str__(self):
        return self.titulo