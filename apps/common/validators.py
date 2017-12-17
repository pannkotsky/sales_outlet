from django.core import validators
from django.utils.translation import ugettext_lazy as _


class DigitValidator(validators.RegexValidator):
    regex = r'^[0-9]*$'
    message = _('Postal code may only contain digits')
