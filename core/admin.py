from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Banners


@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке
    list_display = ('get_html_photo', 'title', 'priority', 'date', 'url')

    # Поля, на которые можно кликнуть для перехода к редактированию
    list_display_links = ('get_html_photo', 'title')

    # Поля, по которым доступен поиск
    search_fields = ('title', 'short_description', 'description')

    # Фильтры в правой колонке
    list_filter = ('date', 'priority')

    # Возможность быстрого редактирования приоритета прямо из списка
    list_editable = ('priority',)

    # Порядок сортировки по умолчанию (сначала высокий приоритет)
    ordering = ('-priority', '-date')

    # Группировка полей внутри формы редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'banner_image', 'get_html_photo')
        }),
        ('Контент и ссылки', {
            'fields': ('short_description', 'description', 'url')
        }),
        ('Настройки отображения', {
            'fields': ('priority',),
            'description': 'Чем выше число, тем раньше отображается баннер.'
        }),
    )

    # Поля только для чтения (нужно для предпросмотра фото)
    readonly_fields = ('get_html_photo', 'date')

    def get_html_photo(self, obj):
        """Метод для отображения миниатюры изображения в админке"""
        if obj.banner_image:
            return mark_safe(f"<img src='{obj.banner_image.url}' width=100>")
        return "Нет фото"

    get_html_photo.short_description = "Миниатюра"



admin.site.site_header = "Панель управления светового оборудование"  # Заголовок вверху
admin.site.site_title = "Световое оборудование"               # Заголовок во вкладке браузера
admin.site.index_title = "Добро пожаловать в админку!"  # Текст на главной странице