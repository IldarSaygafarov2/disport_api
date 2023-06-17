from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_routes),
    path("categories/", views.CategoryListAPIView.as_view()),
    path("categories/<int:pk>/", views.CategoryProductsAPIView.as_view()),
    path("products/", views.ProductListAPIView.as_view()),
    path("products/<int:pk>/", views.ProductDetailAPIView.as_view()),
]

