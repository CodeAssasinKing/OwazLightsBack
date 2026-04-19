from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from site_applications.models import Application

# Register your models here.
@admin.register(Application)
class Application(TranslationAdmin):
    list_display = ('title',"description")
    search_fields = ('title',"description")

    fieldsets = (
        ("Информация", {
            'fields': ('title','description', "poster", "date", "priority"),
        }),
    )
