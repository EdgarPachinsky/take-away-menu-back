from django.contrib import admin

from apps.product_category.models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified')
    list_display_links = ('id', 'name')
    search_fields = ['name']
