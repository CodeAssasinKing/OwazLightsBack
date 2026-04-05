from modeltranslation.translator import TranslationOptions, register
from videos.models import Videos


@register(Videos)
class VideosTranslate(TranslationOptions):
    fields = ('title',)

