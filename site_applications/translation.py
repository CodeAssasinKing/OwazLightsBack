from site_applications.models import Application
from modeltranslation.translator import register, TranslationOptions


@register(Application)
class ApplicationTranslationOptions(TranslationOptions):
    fields = ("title", "description")
