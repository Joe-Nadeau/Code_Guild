from django.urls import path

from .import views

urlpatterns = [
    path('',views.todo_list, name = 'todo_list'),
    path('todo_app/detail/<int:id>', views.detail, name = 'detailed_view'),
    path('todo_app/remove/<int:id>', views.remove, name = 'get_OUT'),
    path('todo_app/update/<int:id>', views.update, name = 'update'),
    path('todo_app/new_task', views.new_task, name = 'new_task'),
]