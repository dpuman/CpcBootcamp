from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.home, name="home"),
    path('teachers/', views.teachers, name='teacher'),
    path('courses/', views.courses, name="courses")

]
