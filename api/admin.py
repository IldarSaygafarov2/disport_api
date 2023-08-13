from django.contrib import admin

from .models import Category, Product, ProductImage, CategoryCharacteristics, CategoryCharacteristicsOptions
import nested_admin


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductOptionsInline(nested_admin.NestedStackedInline):
    model = CategoryCharacteristicsOptions


class OptionsInline(nested_admin.NestedStackedInline):
    model = CategoryCharacteristics
    inlines = [ProductOptionsInline]

# class CategoryCharacteristicsOptionsInline(nested_admin.):
#     model = CategoryCharacteristicsOptions
#     extra = 1

#
# class CategoryCharacteristicsInline(admin.StackedInline):
#     model = CategoryCharacteristics
#     extra = 1
#     inlines = [CategoryCharacteristicsOptionsInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ("pk", "title", "price", "brand", "category")
    # list_editable = ("price", "brand", "category")
    # list_display_links = ("pk", "title")

    inlines = [ProductImageInline,]

    fieldsets = [
        (
            "Общее",
            {
                "fields": ["title", "price", "brand", "vendor_code", "gender", "preview", "category"]
            }
        )
    ]

    list_filter = ("category", "brand")