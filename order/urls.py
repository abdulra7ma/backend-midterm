from django.contrib import admin
from django.urls import include, path

from order import views

urlpatterns = [
    path("create", views.OrderCreateView.as_view(), name="order-create"),
    path("", views.OrderListView.as_view(), name="orders-list"),
    path("<int:pk>/update", views.OrderUpdateView.as_view(), name="order-update"),
    path('<int:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'),

]
