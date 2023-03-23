from django.contrib import admin
from django.urls import path, include

from core.main import views as core_views

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
