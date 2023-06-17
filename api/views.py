from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer


# Create your views here.

@api_view(["GET"])
def get_routes(request):
    routes = [
        "api/v1/categories/",
        "api/v1/categories/<int:pk>/",
        "api/v1/products/",
        "api/v1/products/<int:pk>/",
    ]
    return Response(routes)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductsAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
