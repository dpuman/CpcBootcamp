from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('sum/<int:a>/<int:b>/',views.sum),
    path('sub/<int:a>/<int:b>/', views.sub),

]