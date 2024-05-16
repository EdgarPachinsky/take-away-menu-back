from django.contrib import admin

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'mass', 'portion_for', 'created', 'modified')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'category__name', 'price']
