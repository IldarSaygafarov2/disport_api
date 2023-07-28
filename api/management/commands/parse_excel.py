from django.core.management.base import BaseCommand, CommandError
from api.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass