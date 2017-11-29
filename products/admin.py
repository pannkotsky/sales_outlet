from django.contrib import admin

from .models import Product, Packaging


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')
