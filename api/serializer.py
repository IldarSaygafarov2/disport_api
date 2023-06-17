from rest_framework import serializers
from .models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("pk", "title", "photo")


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("pk", "photo")


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ("pk", "title", "price", "body", "images", "category")