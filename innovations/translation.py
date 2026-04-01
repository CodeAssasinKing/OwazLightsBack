from modeltranslation.translator import TranslationOptions, register
from innovations.models import Innovations

@register(Innovations)
class InnovationsTranslate(TranslationOptions):
    fields = ('name', "description")