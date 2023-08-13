from django.contrib import admin

from .models import Category, Product, ProductImage


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ("pk", "title", "price", "brand", "category")
    # list_editable = ("price", "brand", "category")
    # list_display_links = ("pk", "title")

    inlines = [ProductImageInline, ]

    fieldsets = [
        (
            "Общее",
            {
                "fields": ["title", "price", "brand", "vendor_code", "gender", "preview", "category"]
            }
        )
    ]

    list_filter = ("category", "brand")
