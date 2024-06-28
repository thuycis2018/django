""" models """
from django.db import models


class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=100)

    class Meta:
        """meta"""
        db_table = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        """meta"""
        db_table = 'products'

    def __str__(self):
        return self.name
