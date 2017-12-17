from modeltranslation import translator

from .models import StreetType


@translator.register(StreetType)
class StreetTypeTranslationOptions(translator.TranslationOptions):
    fields = ('short_name', 'full_name')
