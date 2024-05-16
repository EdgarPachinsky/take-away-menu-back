from rest_framework import serializers

from apps.product.models import Product
from apps.product_category.serializers import ProductCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
