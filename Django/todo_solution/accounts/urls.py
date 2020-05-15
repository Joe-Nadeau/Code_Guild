from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name = 'login_page'),
    path('register/', views.register_new_user, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
]