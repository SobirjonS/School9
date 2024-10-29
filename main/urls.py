from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.BannerAPIView.as_view(), name='banner'),
    path('employ/', views.EmployAPIView.as_view(), name='employ'),
    path('news/', views.NewsAPIView.as_view(), name='news'),
    path('background/', views.BackgroundAPIView.as_view(), name='background'),
    path('contact/', views.ContactCreateAPIView.as_view(), name='contact'),
]
