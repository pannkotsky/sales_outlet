from django.contrib import admin

from . import models


@admin.register(models.StreetType)
class StreetTypeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name')


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    pass
