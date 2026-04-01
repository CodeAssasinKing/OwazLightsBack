from django.db import models

# Create your models here.
class Banners(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    banner_image = models.ImageField(upload_to='banners/')
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Баннеры"
        verbose_name = "Баннер"


    def __str__(self):
        return self.title





