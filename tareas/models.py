"""
Definición del Modelo Tareas
---------------------------

Este módulo contiene la definición del modelo de datos Tareas, que se utiliza para representar las tareas en la base de datos.

Importaciones
-------------
models : módulo
    El módulo de Django que contiene clases para definir modelos de bases de datos.

Clase
-----
Tareas : models.Model
    Una clase que define la estructura y los atributos de las tareas en la base de datos.

Atributos
---------
titulo : models.CharField
    Un campo de texto que almacena el título de la tarea.

descripcion : models.TextField
    Un campo de texto largo que almacena la descripción de la tarea.

done : models.BooleanField
    Un campo booleano que indica si la tarea está completada o no.

Métodos
-------
__str__() : str
    Un método especial que devuelve una representación en cadena del objeto, en este caso, devuelve el título de la tarea.

Uso
---
Este modelo se utiliza para representar las tareas en la base de datos. Cada tarea tiene un título, una descripción y un estado de completado.

Ejemplo de uso
--------------
# Crear una nueva tarea en la base de datos
tarea_nueva = Tareas.objects.create(
    titulo="Hacer compras",
    descripcion="Comprar ingredientes para la cena.",
    done=False
)

# Obtener todas las tareas de la base de datos
tareas = Tareas.objects.all()

# Acceder a los atributos de una tarea específica
tarea = tareas[0]
print(tarea.titulo)         # "Hacer compras"
print(tarea.descripcion)    # "Comprar ingredientes para la cena."
print(tarea.done)           # False
"""

from django.db import models

class Tareas(models.Model):
    """
    Modelo que representa las tareas en la base de datos.
    """
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto para la visualiza en el admin.
        """
        return self.titulo
