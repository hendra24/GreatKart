from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price','category', 'stock', 'updated_at')
    search_fields = ['product_name']
    ordering = ['product_name']
    prepopulated_fields = {'slug': ['product_name']}

admin.site.register(Product, ProductAdmin)