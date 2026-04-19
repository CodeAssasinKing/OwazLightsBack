from django.db import models


# Create your models here.
class Application(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to="applications/")
    description = models.TextField()
    date = models.DateField()
    priority = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Applications"
        verbose_name = "Application"
        ordering = ["priority"]

    def __str__(self):
        return self.title
