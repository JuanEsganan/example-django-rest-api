from rest_framework import serializers
from .models import Tareas

class TareaSerializer (serializers.ModelSerializer):
    class Meta:
        #hay que pasarle al modelo
        model = Tareas
        #Estos son los datos que va a convertir rest_framework hacia JSON
        # CAMPO POR CAMPOR: 
        # fields = ("id","titulo", "descripcion", "done") 
        #PERO CUANTO TENGO MUCHOS CAMPOS Y LOS QUIERO TODOS
        fields = "__all__"
