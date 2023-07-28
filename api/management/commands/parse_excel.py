from django.core.management.base import BaseCommand, CommandError
from api.models import Category, Product
from helpers.main import get_data_from_workbook
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def __is_category_exists(self, category):
        obj = Category.objects.filter(title=category).first()
        return True if obj else False

    def __insert_category_if_not_exists(self, category):
        if not self.__is_category_exists(category):
            obj = Category.objects.create(
                title=category,
                photo="",
            )
            obj.save()
            return obj
        return Category.objects.filter(title=category).first()

    def handle(self, *args, **options):
        data = get_data_from_workbook("static/для инфокиоска.xlsx")
        for item in data:
            if item["vendor"] != "Артикул":
                category = self.__insert_category_if_not_exists(
                    category=item["category"]
                )
                try:
                    obj = Product.objects.create(
                        title=item["model"],
                        price=10_000,
                        body=item["body"],
                        vendor_code=item["vendor"],
                        brand=item["brand"],
                        gender=item["gender"],
                        category=category,
                    )
                    obj.save()
                    print(f"Added product {obj.title}")
                except IntegrityError:
                    print("Added already")
                    continue
                except ValueError:
                    print("uncorrect value")
                    continue
