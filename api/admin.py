from django.contrib import admin

from .models import Category, Product, ProductImage, CategoryCharacteristics, CategoryCharacteristicsOptions
from nested_admin.nested import NestedStackedInline, NestedTabularInline


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class CategoryCharacteristicsOptionsInline(admin.StackedInline):
    model = CategoryCharacteristicsOptions
    extra = 1


class CategoryCharacteristicsInline(admin.StackedInline):
    model = CategoryCharacteristics
    extra = 1
    inlines = [CategoryCharacteristicsOptionsInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "brand", "category")
    list_editable = ("price", "brand", "category")
    list_display_links = ("pk", "title")
    list_filter = ("category", "brand")
    # fieldsets = [
    #     (
    #         "Общие данные товара",
    #         {
    #             "fields": ['title', 'body', "price", "brand", "category"]
    #         },
    #     ),
    #     (
    #         "Характеристики",
    #         {
    #             "fields": []
    #         },
    #     ),
    # ]
    inlines = [ProductImageInline, CategoryCharacteristicsInline]
