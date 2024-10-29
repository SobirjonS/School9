from django.db import models

class Banner(models.Model):
    image = models.ImageField(upload_to="banner_images/")
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"


class Employ(models.Model):
    image = models.ImageField(upload_to="employ_images/")
    fullname = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"


class News(models.Model):
    image = models.ImageField(upload_to="news_images/")
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


class Background(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    class Meta:
        verbose_name = "Fon"
        verbose_name_plural = "Fonlar"
        
        
class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        
        return f"{self.name} {self.surname} - {self.created_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontaktlar"