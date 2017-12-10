import datetime

from django.utils.translation import ugettext as _
from django.views.generic import DetailView

from braces.views import StaffuserRequiredMixin

from .models import Product


class ShipmentsView(StaffuserRequiredMixin, DetailView):
    template_name = 'shipments.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ShipmentsView, self).get_context_data(**kwargs)
        context['site_header'] = _('Sales Outlet')
        context['site_title'] = _('Sales Outlet')
        invoices = self.object.invoices.all()
        date_string = self.request.GET.get('date')
        if date_string:
            context['date_string'] = date_string
            date = datetime.datetime.strptime(date_string, '%d.%m.%Y').date()
            context['date'] = date
            invoices = invoices.filter(date=date)
        context['invoices'] = invoices
        total_cost = sum([item.cost() for item in invoices])
        context['total_cost'] = total_cost
        return context
