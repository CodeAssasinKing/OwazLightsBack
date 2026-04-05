from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Gallery, News
from modeltranslation.admin import TranslationAdmin

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ("name",)


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ('get_preview', 'name')
    search_fields = ('name',)
    list_display_links = ("name",)

    def get_preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50 style='object-fit: cover;'>")
        return "Нет фото"

    get_preview.short_description = "Фото"


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    # Основной список
    list_display = ('title', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'short_description', 'content')
    date_hierarchy = 'date'  # Удобная навигация по датам сверху

    # Настройка формы редактирования
    filter_horizontal = ('gallery',"products")  # Удобный выбор фото из галереи
    autocomplete_fields = ('category',)  # Быстрый поиск категории (если их будет много)

    fieldsets = (
        ('Основное', {
            'fields': ('category', 'title', 'date', 'poster')
        }),
        ('Контент', {
            'fields': ('short_description', 'content'),
        }),
        ('Медиа', {
            'fields': ('gallery',),
            'description': 'Выберите изображения из галереи для этой новости'
        }),
        ("Продукты", {
            "fields": ("products",),
            "description": "Выберите продукты для данного новостья"
        })
    )

    readonly_fields = ('date',)