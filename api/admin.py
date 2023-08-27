from django.contrib import admin

from .models import Category, Product, ProductImage, ProductOption, ProductOptionItem


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductOptionItemInline(admin.TabularInline):
    model = ProductOptionItem
    extra = 1


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    inlines = [ProductOptionItemInline,]
    fieldsets = [
        (
            "Общее",
            {
                "fields": ["product", "option_main"]
            }
        )
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "vendor_code", "brand", "category")
    list_editable = ("price", "brand", "vendor_code", "category")
    list_display_links = ("pk", "title")

    inlines = [ProductImageInline, ]

    fieldsets = [
        (
            "Общее",
            {
                "fields": ["title", "price", "brand", "vendor_code", "gender",  "category"]
            },
        ),
    ]

    list_filter = ("category", "brand")
