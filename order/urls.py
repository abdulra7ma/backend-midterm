from django.contrib import admin
from django.urls import include, path

from order import views

urlpatterns = [
    path("create", views.order_create, name="order-create"),
    path("", views.order_list, name="orders-list"),
    path("<int:pk>/update", views.order_update, name="order-update"),
    path('<int:pk>/delete', views.order_delete, name='order-delete'),

]
