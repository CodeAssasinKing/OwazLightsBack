from django.contrib import admin
from .models import UserCredentials


@admin.register(UserCredentials)
class UserCredentialsAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке
    list_display = ('full_name', 'email', 'date')

    # Поля, по которым можно искать (имя или почта)
    search_fields = ('full_name', 'email')

    # Фильтр по дате подписки/регистрации
    list_filter = ('date',)

    # Сортировка: новые записи всегда сверху
    ordering = ('-date',)

    # Поля только для чтения (дату изменять нельзя, она ставится автоматически)
    readonly_fields = ('date',)

    # Ограничение на редактирование (необязательно)
    # Если вы хотите, чтобы почты нельзя было менять вручную в админке,
    # можно добавить:
    # readonly_fields = ('full_name', 'email', 'date')