from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    date = models.DateField(auto_now_add=True)
    poster = models.ImageField(upload_to='images/video-poster/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Видео продуктов"
        verbose_name = "Видео продукта"


    def __str__(self):
        return self.title