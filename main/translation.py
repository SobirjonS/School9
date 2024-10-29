from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)


@register(models.Employ)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('fullname', 'job',)
    
    
@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)
    
    
@register(models.Background)
class BackgroundTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)