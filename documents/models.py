from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from babel.dates import format_date

from customers.models import Customer
from products.models import Product, Packaging


class Contract(models.Model):
    number = models.CharField(verbose_name=_('Number'), max_length=15, primary_key=True)
    date = models.DateField(verbose_name=_('Date'))
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='contracts',
                                 verbose_name=_('Customer'))
    products = models.ManyToManyField(Product, related_name='contracts',
                                      verbose_name=_('Products'))

    def __str__(self):
        return _('#%(number)s from %(date)s, %(customer)s') % {
            'customer': self.customer,
            'number': self.number,
            'date': format_date(self.date, locale=settings.LANGUAGE_CODE)
        }

    def products_list(self):
        return ', '.join(self.products.values_list('name', flat=True))
    products_list.short_description = _('Products list')

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')


class Invoice(models.Model):
    number = models.CharField(verbose_name=_('Number'), max_length=15, primary_key=True)
    date = models.DateField(verbose_name=_('Date'))
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='invoices',
                                 verbose_name=_('Contract'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoices',
                                verbose_name=_('Product'))
    product_quantity = models.IntegerField(verbose_name=_('Product quantity'))
    packaging = models.ForeignKey(Packaging, on_delete=models.SET_NULL, related_name='invoices',
                                  null=True, blank=True, verbose_name=_('Packaging'))

    def __str__(self):
        return _('#%(number)s from %(date)s, %(customer)s') % {
            'customer': self.customer(),
            'number': self.number,
            'date': format_date(self.date, locale=settings.LANGUAGE_CODE)
        }

    def customer(self):
        return self.contract.customer
    customer.short_description = _('Customer')

    def cost(self):
        return self.product.price * self.product_quantity + self.packaging.price
    cost.short_description = _('Cost')

    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')
