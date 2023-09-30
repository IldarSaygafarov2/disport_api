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
            products_list = []
            products = category.products.all()
            for product in products:
                options = [option for option in product.options.all()]
                res = []
                if options:
                    for option in options:
                        print(option.option.all())
                        res.append({
                            "option_category": option.option_main,
                            "option_items": option.option.all()[0].name
                        })

                products_list.append({
                    "product": {
                        "title": product.title,
                        "price": funcs.format_price(product.price),
                        "description": funcs.remove_html_from_text(product.body),
                 	"video": product.video.url if product.video else 'no video',
		        "preview": product.preview.url if product.preview else "static/placeholder.png",
                        "options": res,
                        "images": [
                            image.photo.url if image.photo else "static/placeholder.png"
                            for image in product.images.all()
                        ],
                    }
                })

            data["categories"].append({
                "title": category.title,
                "photo": category.photo.url if category.photo else "static/placeholder.png",
#                'video': category.video.url if category.video else "no video",
                "products": products_list
            })
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
