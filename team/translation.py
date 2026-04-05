from modeltranslation.translator import TranslationOptions, register

from team.models import Teams


@register(Teams)
class TeamsTranslationOptions(TranslationOptions):
    fields = ('full_name', 'job', 'phrase')