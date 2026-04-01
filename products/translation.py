from modeltranslation.translator import TranslationOptions, register
from products.models import ProductSize, ProductCategory, ProductGallery, ProductDocumentations, Products


@register(ProductSize)
class ProductSizeTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductCategory)
class ProductCategoryTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductGallery)
class ProductGalleryTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductDocumentations)
class ProductDocumentationsTranslate(TranslationOptions):
    fields = ('name',)


@register(Products)
class ProductsTranslate(TranslationOptions):
    fields = ('name', 'description', 'short_description',)