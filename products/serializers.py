""" products app serializers """
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ product serializer """
    class Meta:
        """ product serializer meta """
        model = Product
        fields = ['name', 'sku', 'price']
