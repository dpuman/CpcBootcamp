from django.urls import path
from . import views
urlpatterns = [

    path('', views.home),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('shortner/', views.shortner, name="shortner"),
    path('generate/', views.generate, name="generate"),
    path('deleteurl/', views.deleteurl, name="deleteurl"),
    path('<str:query>/', views.home, name="home"),
]
