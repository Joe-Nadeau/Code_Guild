from django.urls import path
from.import views 

app_name = 'library_app'
urlpatterns = [
    path('', views.display_homepage, name = 'homepage'),
    path('books', views.check_out_books, name = 'get_books'),
    path('loan_book/<int:id>/', views.loan_book, name = 'loan_book'),
    path('return_book/<int:id>/', views.return_book, name = 'return_book'),
]
