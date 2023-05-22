from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index.html", views.index),
    path("scope.html", views.scope ),
    path("product.html", views.product),
    path("scrapdata.html", views.scrapdata),
]
