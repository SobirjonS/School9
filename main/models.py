from django.db import models

class Banner(models.Model):
    image = models.ImageField(upload_to="banner_images/")
    title = models.CharField(max_length=255)
    body = models.TextField()


class Employ(models.Model):
    image = models.ImageField(upload_to="employ_images/")
    fullname = models.CharField(max_length=255)
    job = models.CharField(max_length=255)


class News(models.Model):
    image = models.ImageField(upload_to="news_images/")
    title = models.CharField(max_length=255)
    body = models.TextField()

