from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from team.models import Teams, OurValues


# Register your models here.
@admin.register(Teams)
class TeamsAdmin(TranslationAdmin):
    list_display = ('full_name', 'job', 'phrase', 'get_image', 'date')
    search_fields = ('full_name', 'job', 'phrase')


    fieldsets = (
        ("Персональная информация", {
            'fields': ('full_name', 'job', 'phrase')
        }),
        ("Рисунок", {
            'fields': ('image',)
        })
    )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60" style="border-radius: 4px;">')
        return "Нет постера"


@admin.register(OurValues)
class OurValuesAdmin(TranslationAdmin):
    list_display = ("title", 'description')
    list_display_links = ("title", )