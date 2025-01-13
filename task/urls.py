from django.urls import path
from . import views

# Este fichero no se crea automáticamente, por lo que debemos crearlo nosotros.

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Ruta para la vista de lista de tareas
]
