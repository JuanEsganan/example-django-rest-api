"""
Registro del Modelo Tareas en el Sitio de Administración
--------------------------------------------------------

Este módulo registra el modelo Tareas en el sitio de administración de Django para que las tareas puedan ser gestionadas a través de la interfaz de administración web.

Importaciones
-------------
admin : módulo
    El módulo de Django que contiene clases para la configuración del sitio de administración.

Tareas : clase
    La clase de modelo que representa las tareas en la base de datos.

Uso
---
Este módulo se utiliza para registrar el modelo Tareas en el sitio de administración. Una vez registrado, las tareas pueden ser creadas, editadas y eliminadas a través de la interfaz de administración web de Django.

Ejemplo de uso
--------------
# Importar el modelo Tareas y el módulo admin
from .models import Tareas
from django.contrib import admin

# Registrar el modelo Tareas en el sitio de administración
admin.site.register(Tareas)
"""

# Importar el modelo Tareas y el módulo admin
from .models import Tareas
from django.contrib import admin

# Registrar el modelo Tareas en el sitio de administración
admin.site.register(Tareas)
