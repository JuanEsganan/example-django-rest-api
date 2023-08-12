"""
Tarea Views
-----------

Este módulo contiene las vistas que manejan las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para el modelo Tareas.

Clase
-----
TareaView : viewsets.ModelViewSet
    Una clase basada en ModelViewSet que maneja las operaciones CRUD para el modelo Tareas y utiliza TareaSerializer para la serialización.

Atributos
---------
serializer_class : TareaSerializer
    El serializador utilizado para convertir los objetos Tareas en datos JSON y viceversa.

queryset : QuerySet
    Una colección de objetos Tareas consultados de la base de datos.

Uso
---
Esta vista se utiliza para acceder y manipular los datos de las Tareas a través de la API. Proporciona endpoints para crear, listar, recuperar, actualizar y eliminar tareas.

Ejemplo de uso
--------------
# Crear una nueva tarea
POST http://127.0.0.1:8000/tasks/api/v1/tareas/
{
    "titulo": "Hacer compras",
    "descripcion": "Comprar ingredientes para la cena.",
    "completada": False
}

# Obtener la lista de todas las tareas
GET: http://127.0.0.1:8000/tasks/api/v1/tareas/

# Obtener detalles de una tarea específica
GET /api/tareas/1/

# Actualizar una tarea existente
PUT http://127.0.0.1:8000/tasks/api/v1/tareas/1
{
    "titulo": "Hacer compras",
    "descripcion": "Comprar ingredientes para la cena y el almuerzo.",
    "completada": False
}

# Eliminar una tarea
DELETE http://127.0.0.1:8000/tasks/api/v1/tareas/1
"""

from rest_framework import viewsets
from .serializer import TareaSerializer
from .models import Tareas

class TareaView(viewsets.ModelViewSet):
    """
    Vista que maneja las operaciones CRUD para el modelo Tareas.
    """
    serializer_class = TareaSerializer
    queryset = Tareas.objects.all()
