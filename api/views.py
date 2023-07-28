import json
import os

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core import settings
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from django.templatetags.static import static

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

    def get(self, request, *args, **kwargs):
        data = {"categories": []}
        for category in self.get_queryset():
            products = [
                {
                    "product": {
                        "title": product.title,
                        "price": product.price,
                        "description": product.body,
                        "images": [
                            image.photo.url if image.photo else ""
                            for image in product.images.all()
                        ],
                    }
                }
                for product in Product.objects.filter(category=category)
            ]

            item = {
                "title": category.title,
                "photo": category.photo.url if category.photo else "",
                "products": products,
            }
            data["categories"].append(item)

        return Response(data)


class CategoryProductsAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def get_animations(request):
    print(os.path.join(settings.BASE_DIR, "anim.json"))
    return JsonResponse({"file": static("anim.json")})
