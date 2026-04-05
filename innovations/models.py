from django.db import models

# Create your models here.
class Innovations(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='innovations/')
    products = models.ManyToManyField("products.Products",  blank=True, related_name="innovations_list")
    product_description_image = models.ImageField(upload_to='innovations/product_description_image/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Инновации'
        verbose_name = 'Инновации'

    def __str__(self):
        return self.name

