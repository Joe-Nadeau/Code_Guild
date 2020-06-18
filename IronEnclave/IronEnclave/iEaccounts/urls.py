from django.urls import path
from.import views

urlpatterns = [
    path('login/', views.login_user, name = 'login_page'),
    path('register/', views.register_new_user, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('profile/', views.user_profile, name = 'profile'),
    path('updateProf/', views.update_profile, name = 'update_profile'),
    path('updateGraph/', views.update_graph, name = 'update_graph'),
]