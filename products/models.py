from django.db import models
from innovations.models import Innovations
from news.models import News
from videos.models import Videos


class ProductSize(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='product/categories/')

    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='product/galleries/')


    def __str__(self):
        return self.name


class ProductDocumentations(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='product/documentations/')

    def __str__(self):
        return self.name



# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='products/posters/')
    short_description = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    gallery = models.ManyToManyField(ProductGallery, null=True, blank=True)
    innovations = models.ManyToManyField(Innovations, null=True, blank=True)
    video = models.ManyToManyField(Videos, null=True, blank=True)
    news = models.ManyToManyField(News, null=True, blank=True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name


