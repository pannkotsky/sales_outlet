from django import forms

from .models import Invoice


class InvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('number', 'date', 'contract', 'product', 'product_quantity', 'packaging')

    def __init__(self, *args, **kwargs):
        super(InvoiceAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['product'].queryset = self.instance.contract.products
