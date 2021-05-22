"""classthree URL Configuration

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
from one import views as one_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',one_views.index),
    path('<int:a>/<int:b>/<int:c>/',one_views.triangle),
    path('<int:number>',one_views.root),
    path('<int:number1>/<int:number2>',one_views.swap)
]
