from django.urls import path
from.import views 


urlpatterns = [
    path('', views.display_homepage, name = 'homepage'),
    path('books', views.check_out_books, name = 'get_books'),
]
