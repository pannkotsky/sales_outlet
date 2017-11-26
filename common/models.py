from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .validators import DigitValidator


class StreetType(models.Model):
    short_name = models.CharField(verbose_name=_('Short name'), max_length=5, unique=True)
    full_name = models.CharField(verbose_name=_('Full name'), max_length=10, unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Street type')
        verbose_name_plural = _('Street types')


def get_default_street_type():
    try:
        return StreetType.objects.get(short_name_en='st.')
    except StreetType.DoesNotExist:
        return None


class Address(models.Model):
    postal_code = models.CharField(verbose_name=_('Postal code'), max_length=10, validators=[
        validators.MinLengthValidator(4),
        DigitValidator
    ])
    city_name = models.CharField(verbose_name=_('City name'), max_length=15)
    street_type = models.ForeignKey(StreetType, on_delete=models.PROTECT,
                                    default=get_default_street_type,
                                    verbose_name=_('Street type'))
    street_name = models.CharField(verbose_name=_('Street name'), max_length=20)
    street_number = models.PositiveIntegerField(verbose_name=_('Street number'), validators=[
        validators.MaxValueValidator(9999)
    ])
    additional = models.CharField(verbose_name=_('Additional info'), max_length=100, null=True,
                                  blank=True)

    def __str__(self):
        return _('%(postal_code)s %(city_name)s, %(street_name)s %(street_type)s, '
                 '%(street_number)s%(additional)s') % {
            'postal_code': self.postal_code,
            'city_name': self.city_name,
            'street_name': self.street_name,
            'street_type': self.street_type.short_name,
            'street_number': self.street_number,
            'additional': ', ' + self.additional if self.additional else ''
        }

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class BankAccount(models.Model):
    number = models.CharField(verbose_name=_('Account number'), max_length=20, validators=[
        validators.MinLengthValidator(5),
        DigitValidator
    ])
    bank_code = models.CharField(verbose_name=_('Bank code'), max_length=10, validators=[
        validators.MinLengthValidator(4),
        DigitValidator
    ])
    bank_name = models.CharField(verbose_name=_('Bank name'), max_length=50)

    def __str__(self):
        return _('%(number)s in %(bank_name)s, bank code %(bank_code)s') % {
            'number': self.number,
            'bank_name': self.bank_name,
            'bank_code': self.bank_code
        }

    class Meta:
        verbose_name = _('Bank account')
        verbose_name_plural = _('Bank accounts')
        unique_together = ('number', 'bank_code')
