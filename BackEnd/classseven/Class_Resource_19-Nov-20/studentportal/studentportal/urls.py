from django.contrib import admin
from django.urls import path

from student import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.home)
]
