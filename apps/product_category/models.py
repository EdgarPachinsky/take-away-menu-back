from colorfield.fields import ColorField
from django.db import models

from apps.core.models import AbstractBaseModel


class ProductCategory(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    name_translit = models.CharField(max_length=255, null=True, blank=True)
    text_color = ColorField(format='hex', null=True, blank=True)

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name
