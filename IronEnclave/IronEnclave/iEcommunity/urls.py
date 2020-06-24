from django.urls import path
from.import views

app_name = 'iEcommunity'
urlpatterns = [
    path('', views.landing_page, name = 'landing_page'),
    path('home/', views.home_page, name = 'home_page'),
    path('resources/', views.resources, name = 'resources'),
    path('forum_main/', views.forum_main, name = 'forum_main'),
]