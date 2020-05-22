from django.urls import path
from.import views 


urlpatterns = [
    path('', views.display_homepage, name = 'homepage'),
    path('books', views.check_out_books, name = 'get_books'),
    path('add_book/<int:id>/', views.add_book, name = 'add_book'),
    path('return_book/<int:id>/', views.return_book, name = 'return_book'),
]
