from django.shortcuts import render
from .serializer import CategorySerializer
from rest_framework import generics
from .models import Category


# Create your views here.


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
