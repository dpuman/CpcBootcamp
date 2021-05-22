from django.urls import path
from . import views

urlpatterns=[

    path('sum/<int:a>/<int:b>/',views.sum),
    path("sub/<int:a>/<int:b>/",views.sub),
    path("multi/<int:a>/<int:b>/",views.multi),
    path('div/<int:a>/<int:b>/',views.div)
]