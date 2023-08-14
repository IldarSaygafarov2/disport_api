import os

from django.http import JsonResponse
from django.templatetags.static import static
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helpers import main as funcs
from core import settings
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer


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
            products_qs = Product.objects.filter(category=category)
            characteristics = [product.options.all() for product in products_qs]
            options = [{
                "option_category": char.option_main,
                "option_items": [option.name for option in char.option.all()]
            } for char in characteristics[0]]
            print(options)
            products = [
                {
                    "product": {
                        "title": product.title,
                        "price": funcs.format_price(product.price),
                        "description": funcs.remove_html_from_text(product.body),
                        "preview": product.preview.url if product.preview else "static/placeholder.png",
                        "options": options,
                        "images": [
                            image.photo.url if image.photo else "static/placeholder.png"
                            for image in product.images.all()
                        ],
                    }
                }
                for product in products_qs
            ]

            item = {
                "title": category.title,
                "photo": category.photo.url if category.photo else "static/placeholder.png",
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
