from django.db import models

# Create your models here.
class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'


    def __str__(self):
        return self.full_name
