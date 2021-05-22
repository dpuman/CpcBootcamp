from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('students/<str:action>/<int:id>',
         views.students_action_handler, name='students_action'),

    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<str:action>/<int:id>',
         views.teachers_action_handler, name='teachers_action'),

    path('courses/', views.courses, name='courses'),
    path('courses/<str:action>/<int:id>',
         views.courses_action_handler, name='courses_action')
]
