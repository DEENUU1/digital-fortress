from django.core.management.base import BaseCommand
from subscription.services.product import ProductService

class Command(BaseCommand):
    help = "Create Free products"

    def handle(self, *args, **options):
        try:
            ProductService().create_free_product()
            self.stdout.write("Free product created")
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
