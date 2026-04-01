from modeltranslation.translator import TranslationOptions, register
from news.models import Category, Gallery, News


@register(Category)
class CategoryTranslate(TranslationOptions):
    fields = ('name',)


@register(Gallery)
class GalleryTranslate(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslate(TranslationOptions):
    fields = ('title','short_description','content',)