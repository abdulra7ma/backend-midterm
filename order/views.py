from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from .forms import OrderForm
from .models import Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_create.html"
    success_url = reverse_lazy("orders-list")


class OrderCreatedView(TemplateView):
    template_name = "orders/order_created.html"


class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_update.html"
    success_url = reverse_lazy("orders-list")


class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders/order_delete.html"
    success_url = reverse_lazy("orders-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
