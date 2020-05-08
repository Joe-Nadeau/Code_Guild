from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete/<int:id>/', views.delete_url, name = 'delete_url'),
]


    # path('',views.todo_list, name = 'todo_list'),
    # path('detail/<int:id>', views.detail, name = 'detailed_view'),
    # path('remove/<int:id>', views.remove, name = 'get_OUT'),
    # path('update/<int:id>', views.update, name = 'update'),
    # path('new_task', views.new_task, name = 'new_task'),