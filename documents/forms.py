from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.utils.translation import ugettext as _

from products.models import Product
from .models import Invoice, Contract


class InvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('number', 'date', 'contract', 'product', 'product_quantity', 'packaging')

    def __init__(self, *args, **kwargs):
        super(InvoiceAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            try:
                self.fields['product'].queryset = self.instance.contract.products
            except Contract.DoesNotExist:
                pass


def get_product_choices():
    products = Product.objects.all()
    choices = [('', '--------')]
    for product in products:
        choices.append((product.code, str(product)))
    return choices


class ShipmentsFilterForm(forms.Form):
    product = forms.ChoiceField(
        label=_('Product'),
        choices=get_product_choices(),
        required=False,
    )
    date = forms.DateField(
        label=_('Date'),
        widget=AdminDateWidget,
        input_formats=['%d.%m.%Y'],
        required=False
    )
