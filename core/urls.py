from django.contrib import admin
from django.urls import include, path

from core.main import auth as auth_views
from core.main import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("order.urls")),
    path("login/", auth_views.MyLoginView.as_view(), name="login"),
    path('register/', auth_views.SignUpView.as_view(), name='register'),

]
