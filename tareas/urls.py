"""
Configuración de Rutas de la API y Documentación
-----------------------------------------------

Este módulo configura las rutas de la API y proporciona documentación a través de las vistas de Django Rest Framework.

Importaciones
-------------
path : función
    Una función para definir rutas en Django.

include : función
    Una función que permite incluir otras rutas de forma modular.

include_docs_urls : función
    Una función que genera rutas para la documentación de la API.

router : DefaultRouter
    Un enrutador proporcionado por Django Rest Framework para gestionar las rutas de forma automática.

views : módulo
    El módulo que contiene las vistas de la API.

Uso
---
Este archivo configura las rutas para acceder a las diferentes operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de las tareas a través de la API. También proporciona una ruta para acceder a la documentación de la API generada automáticamente.

Rutas
-----
- Ruta base de la API: http://127.0.0.1:8000/tasks/api/v1/
  - Rutas de tareas: http://127.0.0.1:8000/tasks/api/v1/tareas/
- Ruta de documentación: http://127.0.0.1:8000/tasks/docs/

"""

from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tareas import views

# Creación de un enrutador
router = routers.DefaultRouter()
router.register(r"tareas", views.TareaView, "tareas")

urlpatterns = [
    # Rutas de la API
    path("api/v1/", include(router.urls)),
    # Ruta de documentación
    path("docs/", include_docs_urls(title="API Tareas"))
]
