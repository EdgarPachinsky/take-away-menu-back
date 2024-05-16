from django.core.validators import MinValueValidator
from django.db import models

from apps.core.models import AbstractBaseModel
from apps.core.utils.upload_file import instance_file_directory_path
from apps.product_category.models import ProductCategory


class Product(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    name_eng = models.CharField(max_length=255, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False, validators=[MinValueValidator(10)])
    description = models.TextField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1)])
    portion_for = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    image = models.ImageField(max_length=255, upload_to=instance_file_directory_path, null=False, blank=False)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
