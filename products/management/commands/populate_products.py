# products/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Populate the database with categories and associate products'

    def handle(self, *args, **kwargs):
        categories = [
            'Healthcare',
            'Education',
            'Communication',
            'Technology',
        ]

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" created'))

        products = [
            {'name': 'Product A', 'sku': 'SKU001', 'price': 10.99, 'category': 'Healthcare'},
            {'name': 'Product B', 'sku': 'SKU002', 'price': 19.99, 'category': 'Education'},
            {'name': 'Product C', 'sku': 'SKU003', 'price': 15.49, 'category': 'Communication'},
        ]

        for product_data in products:
            category = Category.objects.get(name=product_data['category'])
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                sku=product_data['sku'],
                price=product_data['price'],
                category=category,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" created'))
