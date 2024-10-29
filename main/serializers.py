from rest_framework import serializers
from . import models
        
        
class BannerSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Banner
        fields = ['id', 'title', 'body', 'image_url']
        
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_body(self, obj):
        return {
            'uz': obj.body_uz,
            'ru': obj.body_ru,
            'en': obj.body_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
        
        
class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    
    class Meta:
        model = models.News
        fields = ['id', 'title', 'body', 'image_url']
        
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_body(self, obj):
        return {
            'uz': obj.body_uz,
            'ru': obj.body_ru,
            'en': obj.body_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    
class EmploySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    fullname = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Employ
        fields = ['id', 'fullname', 'job', 'image_url']
        
    def get_fullname(self, obj):
        return {
            'uz': obj.fullname_uz,
            'ru': obj.fullname_ru,
            'en': obj.fullname_en
        }
        
    def get_job(self, obj):
        return {
            'uz': obj.job_uz,
            'ru': obj.job_ru,
            'en': obj.job_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    
class BackgroundSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Background
        fields = ['id', 'title', 'body', 'image_url']
        
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_body(self, obj):
        return {
            'uz': obj.body_uz,
            'ru': obj.body_ru,
            'en': obj.body_en
        }
    
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['name', 'surname', 'age', 'number', 'created_at']
        read_only_fields = ['created_at']