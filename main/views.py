from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .import models


class BannerAPIView(APIView):
    def get(self,request):
        banner = models.Banner.objects.all()    
        serializer = serializers.BannerSerializer(banner, many=True, context={'request':request})
        return Response(serializer.data)
    
    
class EmployAPIView(APIView):
    def get(self,request):
        employ = models.Employ.objects.all()    
        serializer = serializers.EmploySerializer(employ, many=True, context={'request':request})
        return Response(serializer.data)
    
    
class NewsAPIView(APIView):
    def get(self,request):
        news = models.News.objects.all()   
        serializer = serializers.NewsSerializer(news, many=True, context={'request':request})
        return Response(serializer.data)