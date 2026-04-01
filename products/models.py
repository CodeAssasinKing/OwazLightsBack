from django.db import models


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

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='products/posters/')
    short_description = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)



    def __str__(self):
        return self.name


