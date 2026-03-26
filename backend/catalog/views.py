import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from catalog.pagination import CustomPagination

from catalog.models import Product, Category
from catalog.serializers import ProductSerializer, CategorySerializer
from rest_framework import mixins


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_id = django_filters.NumberFilter(field_name='category_id')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category_id']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = ProductFilter

    search_fields = ('name', 'tags')
    ordering_fields = ('price', 'created_at')

class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer