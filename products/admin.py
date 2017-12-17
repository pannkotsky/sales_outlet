from django.contrib import admin

from documents.admin import InvoiceInline
from .models import Product, Packaging


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')
    inlines = [
        InvoiceInline
    ]


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')
