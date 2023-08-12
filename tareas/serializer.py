"""
Tarea Serializer
----------------

Este módulo contiene la definición del serializador TareaSerializer, que convierte objetos Tareas en representaciones JSON y viceversa.

Importaciones
-------------
serializers : módulo
    El módulo de Django Rest Framework que contiene clases para la serialización de datos.

Tareas : clase
    La clase de modelo que representa las tareas en la base de datos.

Clase
-----
TareaSerializer : serializers.ModelSerializer
    Una clase que define la forma en que los objetos Tareas se convierten en JSON y viceversa.

Atributos
---------
model : Tareas
    El modelo que se utilizará para la serialización.

fields : str
    Los campos que se incluirán en la serialización. En este caso, se incluyen todos los campos del modelo.

Uso
---
Este serializador se utiliza para convertir objetos Tareas en representaciones JSON y para realizar la deserialización de datos JSON en objetos Tareas. Permite la comunicación entre la API y los objetos de la base de datos.

Ejemplo de uso
--------------
# Importar el serializador TareaSerializer y el modelo Tareas
from .models import Tareas
from rest_framework import serializers

# Crear una instancia del serializador para un objeto Tareas
tarea = Tareas.objects.get(pk=1)
serializer = TareaSerializer(tarea)

# Serializar el objeto Tareas en formato JSON
json_data = serializer.data

# Deserializar datos JSON en un objeto Tareas
new_data = {
    "titulo": "Nueva tarea",
    "descripcion": "Descripción de la nueva tarea.",
    "done": False
}
deserializer = TareaSerializer(data=new_data)
if deserializer.is_valid():
    tarea_nueva = deserializer.save()
"""

from rest_framework import serializers
from .models import Tareas

class TareaSerializer(serializers.ModelSerializer):
    """
    Serializador para objetos Tareas.
    """
    class Meta:
        #hay que pasarle al modelo
        model = Tareas
        #Estos son los datos que va a convertir rest_framework hacia JSON
        # CAMPO POR CAMPO: 
        # fields = ("id","titulo", "descripcion", "done") 
        #PERO CUANTO TENGO MUCHOS CAMPOS Y LOS QUIERO TODOS
        fields = "__all__"
