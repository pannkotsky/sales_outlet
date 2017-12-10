from django.contrib import admin
from django.db.models import ForeignKey, ManyToManyField

from select2.forms import Select, SelectMultiple

from .forms import InvoiceAdminForm
from .models import Contract, Invoice


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'customer', 'products_list')
    formfield_overrides = {
        ForeignKey: {'widget': Select},
        ManyToManyField: {'widget': SelectMultiple},
    }


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm
    list_display = ('number', 'date', 'customer', 'product', 'product_quantity', 'packaging',
                    'cost')
    formfield_overrides = {
        ForeignKey: {'widget': Select},
    }
    list_filter = ('date', 'product')
