from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Innovations
from modeltranslation.admin import TranslationAdmin

@admin.register(Innovations)
class InnovationsAdmin(TranslationAdmin):
    # Что отображаем в списке
    list_display = ('get_preview', 'name', 'date', 'get_products_count')

    # Поиск по названию и описанию
    search_fields = ('name', 'description')

    # Фильтр по дате создания
    list_filter = ('date',)

    # Удобный интерфейс выбора продуктов (горизонтальный фильтр)
    filter_horizontal = ('products',)

    # Поля только для чтения (для превью картинок)
    readonly_fields = ('get_preview', 'get_full_description_image', 'date')

    # Группировка полей
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'date')
        }),
        ('Изображения', {
            'fields': (
                ('image', 'get_preview'),
                ('product_description_image', 'get_full_description_image'),
            ),
        }),
        ('Связи', {
            'fields': ('products',),
            'description': 'Выберите товары, к которым относится данная инновация'
        }),
    )

    def get_preview(self, obj):
        """Превью основного изображения"""
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=70 style='border-radius: 5px;'>")
        return "Нет фото"

    get_preview.short_description = "Превью"

    def get_full_description_image(self, obj):
        """Превью дополнительного изображения"""
        if obj.product_description_image:
            return mark_safe(f"<img src='{obj.product_description_image.url}' width=150>")
        return "Нет фото"

    get_full_description_image.short_description = "Фото описания продукта"

    def get_products_count(self, obj):
        """Отображение количества привязанных продуктов"""
        return obj.products.count()

    get_products_count.short_description = "Кол-во товаров"