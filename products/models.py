from django.db import models
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import MoneyField


class Item(models.Model):
    code = models.CharField(verbose_name=_('Code'), max_length=30, primary_key=True)
    name = models.CharField(verbose_name=_('Name'), max_length=50, unique=True)
    price = MoneyField(verbose_name=_('Price'), max_digits=12, decimal_places=2,
                       default_currency='UAH')

    def __str__(self):
        return '{} {}'.format(self.name, self.code)

    class Meta:
        abstract = True


class Product(Item):
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Packaging(Item):
    class Meta:
        verbose_name = _('Packaging')
        verbose_name_plural = _('Packaging')
