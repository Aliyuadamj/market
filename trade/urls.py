from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name="products"),
    path("products/<int:pk>", views.product, name="product"),
    path('categories/', views.categorys, name="categotries"),
    path('categories/<int:pk>',views.category,name="category" ),
]