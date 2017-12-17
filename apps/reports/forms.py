from django.contrib.admin.widgets import AdminDateWidget
from django.db.utils import ProgrammingError
from django import forms
from django.utils.translation import ugettext as _

from products.models import Product


def get_product_choices():
    try:
        products = Product.objects.all()
        choices = [('', '--------')]
        for product in products:
            choices.append((product.code, str(product)))
        return choices
    except ProgrammingError:
        return []


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
