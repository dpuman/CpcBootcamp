from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('check/<int:number>/',views.evenodd)
]