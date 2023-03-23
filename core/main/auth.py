from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "auth/login.html"
    success_url = reverse_lazy("orders-list")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "auth/register.html"
