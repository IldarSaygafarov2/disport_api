from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoryListAPIView.as_view()),
    path("products/", views.ProductListAPIView.as_view())
]

