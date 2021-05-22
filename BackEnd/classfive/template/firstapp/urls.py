from django.urls import path
from . import views

urlpatterns=[
    path('form/',views.form),
    path('post/',views.getpost),
    path('sum/',views.sum)
]