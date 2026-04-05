from modeltranslation.translator import TranslationOptions, register
from core.models import Banners


@register(Banners)
class BannersTranslate(TranslationOptions):
    fields = ('title', "short_description")

