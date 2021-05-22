from django.urls import path
from replace import views

urlpatterns = [
    path('', views.index, name='index')
]
