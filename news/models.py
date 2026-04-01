from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Категории новостей"
        verbose_name = "Категория новостя"

    def __str__(self):
        return self.name



class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name_plural = "Галерея новостей"
        verbose_name = "Галерея новостей"

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gallery = models.ManyToManyField(Gallery, null=True, blank=True)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

