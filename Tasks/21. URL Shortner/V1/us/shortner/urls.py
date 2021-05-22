from django.urls import path
from . import views
urlpatterns = [
    path('', views.shortner, name='shortner'),
    path('short/<str:token>', views.home, name='home'),
]
