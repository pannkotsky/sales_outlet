from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CustomersConfig(AppConfig):
    name = 'customers'
    verbose_name = _('Customers')
