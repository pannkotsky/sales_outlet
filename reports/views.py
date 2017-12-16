import datetime

from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic import ListView

from braces.views import StaffuserRequiredMixin

from documents.models import Invoice
from products.models import Product
from .forms import ShipmentsFilterForm


class ShipmentsView(StaffuserRequiredMixin, ListView):
    template_name = 'shipments.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ShipmentsView, self).get_context_data(**kwargs)
        context['site_header'] = _('Sales Outlet')
        context['site_title'] = _('Sales Outlet')

        date_string = self.request.GET.get('date')
        if date_string:
            context['date_string'] = date_string
            date = datetime.datetime.strptime(date_string, '%d.%m.%Y').date()
            context['date'] = date
            invoices = Invoice.objects.filter(date=date)
        else:
            date = None
            invoices = Invoice.objects.all()

        products = Product.objects.shipped(date=date)

        product_code = self.request.GET.get('product')
        if product_code:
            products = products.filter(pk=product_code)
            product = get_object_or_404(Product, code=product_code)
            context['product'] = product
            invoices = invoices.filter(product__code=product_code)
            context['total_quantity'] = sum(invoices.values_list('product_quantity', flat=True))

        context['products'] = products
        context['shipments_stats'] = {}
        context['invoices'] = {}
        for p in products:
            context['shipments_stats'][p.code] = p.shipment_stats(date)
            context['invoices'][p.code] = invoices.filter(product=p)

        context['total_cost'] = sum([item.cost() for item in invoices])

        context['form'] = ShipmentsFilterForm(initial={
            'product': product_code or '',
            'date': date_string or ''
        })
        return context
