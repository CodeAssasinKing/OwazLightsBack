from django.db import models
from products.models import Products
# Create your models here.
class Innovations(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='innovations/')
    products = models.ManyToManyField(Products, null=True, blank=True)
    product_description_image = models.ImageField(upload_to='innovations/product_description_image/')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Инновации'
        verbose_name = 'Инновации'

    def __str__(self):
        return self.name

