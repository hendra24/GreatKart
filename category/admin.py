from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','category_name', 'slug', 'description')
    search_fields = ['category_name']
    ordering = ['category_name']
    prepopulated_fields = {'slug':['category_name']}

# Register your models here.
admin.site.register(Category, CategoryAdmin)