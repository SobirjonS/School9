from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'body_uz',)}),
        (_('Russian'), {'fields': ('title_ru', 'body_ru',)}),
        (_('English'), {'fields': ('title_en', 'body_en',)}),
        (_('Image'), {'fields': ('image',)}),
    )


@admin.register(models.Employ)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('fullname_uz', 'fullname_ru', 'fullname_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('fullname_uz', 'job_uz',)}),
        (_('Russian'), {'fields': ('fullname_ru', 'job_ru',)}),
        (_('English'), {'fields': ('fullname_en', 'job_en',)}),
        (_('Image'), {'fields': ('image',)}),
    )
    

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'body_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'body_ru')}),
        (_('English'), {'fields': ('title_en', 'body_en')}),
        (_('Image'), {'fields': ('image',)}),
    )
    
    
@admin.register(models.Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'body_uz',)}),
        (_('Russian'), {'fields': ('title_ru', 'body_ru',)}),
        (_('English'), {'fields': ('title_en', 'body_en',)}),
        (_('Image'), {'fields': ('image',)}),
    )
    

admin.site.register(models.Contact)