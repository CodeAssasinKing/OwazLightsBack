from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Gallery, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('get_preview', 'name')
    search_fields = ('name',)

    def get_preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50 style='object-fit: cover;'>")
        return "Нет фото"

    get_preview.short_description = "Фото"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # Основной список
    list_display = ('title', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'short_description', 'content')
    date_hierarchy = 'date'  # Удобная навигация по датам сверху

    # Настройка формы редактирования
    filter_horizontal = ('gallery',)  # Удобный выбор фото из галереи
    autocomplete_fields = ('category',)  # Быстрый поиск категории (если их будет много)

    fieldsets = (
        ('Основное', {
            'fields': ('category', 'title', 'date')
        }),
        ('Контент', {
            'fields': ('short_description', 'content'),
        }),
        ('Медиа', {
            'fields': ('gallery',),
            'description': 'Выберите изображения из галереи для этой новости'
        }),
    )

    readonly_fields = ('date',)