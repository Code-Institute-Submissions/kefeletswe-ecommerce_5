from django.contrib import admin
from .models import Category, Products



# Register your models here.
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'image', 'category', 'in_stock']
    list_editable = ['price', 'in_stock']


