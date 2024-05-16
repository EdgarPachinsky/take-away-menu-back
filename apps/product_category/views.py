from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.product_category import serializers
from apps.product_category.models import ProductCategory


class ProductCategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.ProductCategorySerializer
    queryset = ProductCategory.objects.all()
