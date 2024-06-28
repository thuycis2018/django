""" urls """
from django.urls import path
from .views import (ProductListView, ProductBulkCreateView,
                    ProductBulkUpdateView, ProductBulkDeleteView,
                    ProductDetailView)


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/bulk-create/', ProductBulkCreateView.as_view(), name='product-bulk-create'),
    path('products/bulk-update/', ProductBulkUpdateView.as_view(), name='product-bulk-update'),
    path('products/bulk-delete/', ProductBulkDeleteView.as_view(), name='product-bulk-delete'),
]
