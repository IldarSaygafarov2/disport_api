from rest_framework import generics

from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer


# Create your views here.


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
