""" Tests """
# pylint: disable=E1101
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Category


class ProductTests(TestCase):
    """
    This module provides tests for Products.
    """
    def setUp(self):
        """ Create test data """
        # Create categories
        self.category1 = Category.objects.create(name='Healthcare')
        self.category2 = Category.objects.create(name='Education')
        self.category3 = Category.objects.create(name='Communication')

        # Initial setup for creating some test data
        self.product1 = Product.objects.create(name='Product A', sku='SKU001', price=10.99, category=self.category1)
        self.product2 = Product.objects.create(name='Product B', sku='SKU002', price=19.99, category=self.category2)
        self.product3 = Product.objects.create(name='Product C', sku='SKU003', price=15.49, category=self.category3)

        self.bulk_product_data = [
            {"name": "Product D", "sku": "SKU004", "price": 22.99, "category": self.category1.id},
            {"name": "Product E", "sku": "SKU005", "price": 24.99, "category": self.category2.id},
        ]

        self.bulk_update_data = [
            {"id": self.product1.id, "name": "Bulk Updated Product A", "sku": "SKU001",
             "price": 13.99, "category": self.category1.id},
            {"id": self.product2.id, "name": "Bulk Updated Product B", "sku": "SKU002",
             "price": 20.99, "category": self.category2.id},
        ]

        self.bulk_delete_data = [
            {"id": self.product1.id},
            {"id": self.product2.id}
        ]

    def test_product_list(self):
        """ Test retrieving the list of products """
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)  # Assuming 3 products were created in setUp

    def test_product_list_pagination(self):
        """ Test pagination """
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)  # Check if results are paginated

    def test_product_list_filter_by_sku(self):
        """ Test filtering by SKU """
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url, {'sku': 'SKU001'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['sku'], 'SKU001')

    def test_product_list_order_by_sku(self):
        """ Test ordering by SKU """
        client = APIClient()
        url = reverse('product-list')
        response = client.get(url, {'ordering': 'sku'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        skus = [product['sku'] for product in response.data['results']]
        self.assertEqual(skus, ['SKU001', 'SKU002', 'SKU003'])  # Assuming alphabetical order

    def test_bulk_create_products(self):
        """ Test creating multiple products """
        url = reverse('product-bulk-create')
        response = self.client.post(url, self.bulk_product_data, content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 5)
        self.assertEqual(Product.objects.get(sku='SKU004').name, 'Product D')

    def test_get_product_detail(self):
        """ Test getting one product """
        url = reverse('product-detail', kwargs={'pk': self.product1.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product A')

    def test_bulk_update_products(self):
        """ Test updating multiple products """
        url = reverse('product-bulk-update')
        response = self.client.put(url, data=self.bulk_update_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.assertEqual(self.product1.name, 'Bulk Updated Product A')
        self.assertEqual(self.product2.name, 'Bulk Updated Product B')

    def test_bulk_delete_products(self):
        """ Test deleting multipe products """
        url = reverse('product-bulk-delete')
        response = self.client.delete(url, self.bulk_delete_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
