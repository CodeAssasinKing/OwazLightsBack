from modeltranslation.translator import TranslationOptions, register
from products.models import ProductSize, ProductCategory, ProductGallery, ProductDocumentations, Products, \
    ProductSubcategory


@register(ProductSize)
class ProductSizeTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductCategory)
class ProductCategoryTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductSubcategory)
class ProductSubcategoryTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductGallery)
class ProductGalleryTranslate(TranslationOptions):
    fields = ('name',)


@register(ProductDocumentations)
class ProductDocumentationsTranslate(TranslationOptions):
    fields = ('name', "description", )


@register(Products)
class ProductsTranslate(TranslationOptions):
    fields = ('name', 'description', 'short_description',)