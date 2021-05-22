from django.contrib import admin
from django.urls import path

from students import views as students_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:action>/<str:sid>', students_views.action_handler),
    path('', students_views.all_students),
]
