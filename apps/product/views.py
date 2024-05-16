from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.product import serializers
from apps.product.models import Product


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
