from rest_framework import viewsets
from .serializer import TareaSerializer
from .models import Tareas

#con una clase hacemos toddas las opeaciones CRUD

class TareaView(viewsets.ModelViewSet):
    serializer_class= TareaSerializer
    queryset = Tareas.objects.all()