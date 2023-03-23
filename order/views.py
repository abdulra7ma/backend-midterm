from django.shortcuts import redirect, render

from .forms import OrderForm
from .models import Order


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_created")
    else:
        form = OrderForm()
    return render(request, "order_create.html", {"form": form})


def order_created(request):
    return render(request, "order_created.html")


def order_list(request):
    orders = Order.objects.all()
    return render(request, "order_list.html", {"orders": orders})
