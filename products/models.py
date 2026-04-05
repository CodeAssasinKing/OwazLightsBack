from django.db import models
from innovations.models import Innovations
from news.models import News
from videos.models import Videos


class ProductSize(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Размер продуктов"
        verbose_name = "Размер продукта"

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='product/categories/')

    class Meta:
        verbose_name_plural = "Категории продуктов"
        verbose_name = "Категория продукта"

    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='product/galleries/')


    class Meta:
        verbose_name_plural = "Галерея продуктов"
        verbose_name = "Галерея продуктов"

    def __str__(self):
        return self.name


class ProductDocumentations(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='product/documentations/')


    class Meta:
        verbose_name_plural = "Документации к продуктам"
        verbose_name = "Документация к продукту"

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
    gallery = models.ManyToManyField(ProductGallery,  blank=True)
    innovations = models.ManyToManyField(Innovations, blank=True, related_name="products_list")
    product_documentations = models.ManyToManyField(ProductDocumentations, blank=True, related_name="products_list")
    video = models.ManyToManyField(Videos, blank=True)
    news = models.ManyToManyField(News, blank=True, related_name="products_list")
    date = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Продукты"
        verbose_name = "Продукт"

    def __str__(self):
        return self.name


