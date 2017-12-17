from django.contrib import admin

from documents.admin import ContractInline
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'address', 'account')
    inlines = [ContractInline]
