from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', required=False, allow_null=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category_id', 'tags', 'created_at']