from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('sku', 'name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)