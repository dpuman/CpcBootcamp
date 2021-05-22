from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('products/search/', views.search, name="search"),
    path('products/<slug:medicine_name>/', views.selected_product, name="selected product"),
]
