from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import Address, BankAccount


class Customer(models.Model):
    code = models.CharField(verbose_name=_('Code'), max_length=20, primary_key=True)
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True,
                                verbose_name=_('Address'))
    account = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True,
                                verbose_name=_('Bank account'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
