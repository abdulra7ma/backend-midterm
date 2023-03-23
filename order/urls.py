from django.contrib import admin
from django.urls import path, include

from order import views

urlpatterns = [
    path("create-order", views.order_create, name="order-create"),
    path("list", views.order_list,  name="orders-list"),
]
