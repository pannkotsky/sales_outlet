from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from babel.dates import format_date

from customers.models import Customer
from products.models import Product


class Contract(models.Model):
    number = models.CharField(verbose_name=_('Number'), max_length=15, primary_key=True)
    date = models.DateField(verbose_name=_('Date'))
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name=_('Customer'))
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('Product'))

    def __str__(self):
        return _('#%(number)s from %(date)s, %(customer)s') % {
            'customer': self.customer,
            'number': self.number,
            'date': format_date(self.date, locale=settings.LANGUAGE_CODE)
        }

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')
