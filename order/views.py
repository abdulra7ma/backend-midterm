from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderForm
from .models import Order


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders-list")
    else:
        form = OrderForm()
    return render(request, "orders/order_create.html", {"form": form})


def order_created(request):
    return render(request, "orders/order_created.html")


def order_list(request):
    orders = Order.objects.all()
    return render(request, "orders/order_list.html", {"orders": orders})


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orders-list")
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/order_update.html", {"form": form})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('orders-list')