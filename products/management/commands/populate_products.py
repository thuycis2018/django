from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Populate products table with initial data'

    def handle(self, *args, **kwargs):
        # Add your product creation logic here
        products = [
            {'name': 'Product 6', 'sku': 'SKU006', 'price': 10.00},
            {'name': 'Product 7', 'sku': 'SKU007', 'price': 11.00},
            {'name': 'Product 8', 'sku': 'SKU008', 'price': 19.00},
            {'name': 'Product 9', 'sku': 'SKU009', 'price': 22.00},
            {'name': 'Product 10', 'sku': 'SKU0010', 'price': 30.00},
            {'name': 'Product 11', 'sku': 'SKU0011', 'price': 27.00},
            {'name': 'Product 12', 'sku': 'SKU0012', 'price': 47.00},
            # Add more products as needed
        ]
        
        for product_data in products:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS('Products successfully populated'))
