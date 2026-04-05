from django.db import models

# Create your models here.
class Teams(models.Model):
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    phrase = models.TextField()
    image = models.ImageField(upload_to='teams/')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Наша команда'
        ordering = ('-date',)
        verbose_name = 'Команду'

    def __str__(self):
        return self.full_name
