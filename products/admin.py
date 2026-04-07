from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    ProductSize,
    ProductCategory,
    ProductGallery,
    ProductDocumentations,
    Products,
    ProductSubcategory,
)
from modeltranslation.admin import TranslationAdmin


# Настройка вспомогательных моделей
@admin.register(ProductSize)
class ProductSizeAdmin(TranslationAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ("get_preview", "name")
    search_fields = ("name",)

    def get_preview(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" width="50">')
        return "Нет фото"

    get_preview.short_description = "Постер"


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(TranslationAdmin):
    list_display = ("name", "category", "poster")
    search_fields = ("name",)

    def get_poster(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" width="50">')
            return "Нет фото"


@admin.register(ProductGallery)
class ProductGalleryAdmin(TranslationAdmin):
    list_display = ("get_preview", "name")

    def get_preview(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" width="50">')
        return "Нет фото"

    get_preview.short_description = "Фото"


@admin.register(ProductDocumentations)
class ProductDocumentationsAdmin(TranslationAdmin):
    list_display = ("name", "file")


# Основная настройка ТОВАРОВ
@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    # Что видим в списке
    list_display = (
        "get_poster_preview",
        "name",
        "category",
        "subcategory",
        "size",
        "date",
    )
    list_filter = ("category", "size", "date")
    search_fields = ("name", "description", "short_description")

    # Удобный интерфейс для связей ManyToMany
    filter_horizontal = ("gallery", "innovations", "video", "news", "product_documentations")

    # Автозаполнение (если категорий или размеров станет очень много)
    autocomplete_fields = ("category", "subcategory", "size")

    # Группировка полей (Fieldsets)
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("name", "category", "subcategory", "size", "date")},
        ),
        (
            "Контент",
            {
                "fields": ("short_description", "description", "product_documentations"),
            },
        ),
        (
            "Медиа и Визуал",
            {
                "fields": (("poster", "get_poster_preview"), "gallery", "video"),
            },
        ),
        (
            "Связанный контент",
            {
                "classes": ("collapse",),  # Этот блок можно будет сворачивать
                "fields": ("innovations", "news"),
                "description": "Новости и инновации, связанные с этим продуктом",
            },
        ),
    )

    readonly_fields = ("get_poster_preview", "date")

    def get_poster_preview(self, obj):
        if obj.poster:
            return mark_safe(
                f'<img src="{obj.poster.url}" width="60" style="border-radius: 4px;">'
            )
        return "Нет постера"

    get_poster_preview.short_description = "Превью"
