from django.utils.translation import ugettext_lazy as _

from documents.models import Invoice


class Shipment(Invoice):
    class Meta:
        proxy = True
        verbose_name = _('Shipment')
        verbose_name_plural = _('Shipments')
