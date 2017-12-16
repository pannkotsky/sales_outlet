from django.db.models import Manager

from documents.models import Invoice


class ProductManager(Manager):
    def shipped(self, date=None):
        invoices = Invoice.objects.all()
        if date:
            invoices = invoices.filter(date=date)
        shipped_codes = invoices.order_by('product').values_list(
            'product__code', flat=True).distinct()
        return self.filter(code__in=shipped_codes)
