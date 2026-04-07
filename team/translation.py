from modeltranslation.translator import TranslationOptions, register

from team.models import Teams, OurValues


@register(Teams)
class TeamsTranslationOptions(TranslationOptions):
    fields = ('full_name', 'job', 'phrase')



@register(OurValues)
class OurValuesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')