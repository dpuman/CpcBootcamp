"""basicrouting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapplication import views as firstapplication_views
from secondapp import views as secondapp_view
from thirdapp import views as thirdapp_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstapplication_views.index),
    path('firsthome/',firstapplication_views.home),
    path('firstabout/',firstapplication_views.about),
    path('firstcontact/',firstapplication_views.contact),
    path('secondhome/',secondapp_view.home),
    path('secondabout/',secondapp_view.about),
    path('secondcontact/',secondapp_view.contact),
    path('thirdhome/',thirdapp_view.home),
    path('thirdabout/',thirdapp_view.about),
    path('thirdcontact/',thirdapp_view.contact),

]
