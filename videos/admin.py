from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Videos
from modeltranslation.admin import TranslationAdmin


@admin.register(Videos)
class VideosAdmin(TranslationAdmin):
    # Поля в списке: превью плеера, название и дата
    list_display = ('get_video_player', 'title', 'date')
    list_display_links = ('title',)
    # Поиск по названию
    search_fields = ('title',)

    # Фильтр по дате загрузки
    list_filter = ('date',)

    # Поля только для чтения (для отображения плеера в форме редактирования)
    readonly_fields = ('get_video_player', 'date')

    # Группировка полей в форме
    fieldsets = (
        ('Информация о видео', {
            'fields': ('title', 'date')
        }),
        ('Файл и предпросмотр', {
            'fields': ('file', 'get_video_player', 'poster'),
        }),
    )

    def get_video_player(self, obj):
        """Метод для вставки HTML5 видеоплеера в админку"""
        if obj.file:
            return mark_safe(
                f'<video src="{obj.file.url}" width="200" height="120" controls '
                f'style="background:#000; border-radius:5px;">'
                f'Ваш браузер не поддерживает видео.'
                f'</video>'
            )
        return "Файл не загружен"

    get_video_player.short_description = "Просмотр видео"