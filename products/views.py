from rest_framework import generics, pagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(pagination.PageNumberPagination):
    # http://127.0.0.1:8000/api/products/?page=2&page_size=5
    page_size = 10  # Number of products per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of products per page

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination  # Use custom pagination class

    @swagger_auto_schema(
        operation_description="Retrieve a list of products with optional filters and pagination.",
        manual_parameters=[
            openapi.Parameter('sku', openapi.IN_QUERY, description="Filter by SKU", type=openapi.TYPE_STRING),
            openapi.Parameter('min_price', openapi.IN_QUERY, description="Minimum price", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_price', openapi.IN_QUERY, description="Maximum price", type=openapi.TYPE_NUMBER),
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
            openapi.Parameter('page_size', openapi.IN_QUERY, description="Number of items per page", type=openapi.TYPE_INTEGER),
        ],
        responses={200: ProductSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.all()

        # Retrieve and filter by SKU if provided in query parameters
        sku = self.request.query_params.get('sku')
        if sku:
            queryset = queryset.filter(sku__icontains=sku)

        # Retrieve and filter by price range if provided in query parameters
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        # Order queryset by SKU
        queryset = queryset.order_by('sku')

        return queryset
