from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    
    
class BackgroundAPIView(APIView):
    def get(self,request):
        background = models.Background.objects.all()    
        serializer = serializers.BackgroundSerializer(background, many=True, context={'request':request})
        return Response(serializer.data) 
    
    
class ContactCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)