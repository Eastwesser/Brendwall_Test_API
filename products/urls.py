from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.product_list_create, name='product_list_create'),
    path('', views.index, name='index'),
]
