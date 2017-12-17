import datetime

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

from braces.views import StaffuserRequiredMixin

from documents.models import Invoice
from products.models import Product
from .forms import ShipmentsFilterForm


class ShipmentsView(StaffuserRequiredMixin, TemplateView):
    template_name = 'shipments.html'

    def get_context_data(self, **kwargs):
        context = super(ShipmentsView, self).get_context_data(**kwargs)
        context['site_header'] = _('Sales Outlet')
        context['site_title'] = _('Sales Outlet')

        invoices = Invoice.objects.all()

        date_string = self.request.GET.get('date')
        if date_string:
            context['date_string'] = date_string
            date = datetime.datetime.strptime(date_string, '%d.%m.%Y').date()
            context['date'] = date
            invoices = invoices.filter(date=date)

        products = Product.objects.all()

        product_code = self.request.GET.get('product')
        if product_code:
            products = products.filter(pk=product_code)
            product = get_object_or_404(Product, code=product_code)
            context['product'] = product
            invoices = invoices.filter(product__code=product_code)
            context['total_quantity'] = invoices.aggregate(
                Sum('product_quantity'))['product_quantity__sum']

        context['products'] = products
        context['product_shipped'] = {}
        context['invoices'] = {}
        context['product_quantity'] = {}
        context['product_cost'] = {}
        for p in products:
            product_invoices = invoices.filter(product=p)
            context['product_shipped'][p.code] = bool(product_invoices)
            context['invoices'][p.code] = product_invoices
            context['product_quantity'][p.code] = product_invoices.aggregate(
                Sum('product_quantity'))['product_quantity__sum']
            context['product_cost'][p.code] = sum([item.cost() for item in product_invoices])

        context['total_cost'] = sum([item.cost() for item in invoices])

        context['form'] = ShipmentsFilterForm(initial={
            'product': product_code or '',
            'date': date_string or ''
        })
        return context
