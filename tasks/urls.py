from django.urls import path
from .views import list_tasks, create_tasks, delete_task,edit_task

urlpatterns = [
    path('', list_tasks),

# esta funcion es para asignaar un nombre y usarlo en el html. Asi nos cogera la ruta asi la cambiemos (  path('example_name/', create_tasks, name='create_task'),  )
    path('new_task/', create_tasks, name='create_task'),
# funcion para eliminar de la base de datos:
    path('delete_task/<int:task_id>/',delete_task, name='delete_task' ),

    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
]