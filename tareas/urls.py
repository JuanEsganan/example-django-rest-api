from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tareas import views

#api version

router = routers.DefaultRouter()
router.register(r"tareas", views.TareaView, "tareas")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="API Tareas"))
    ]

#Con este archivo se estan creando todas las rutas GET-POST-PUT-DELETE