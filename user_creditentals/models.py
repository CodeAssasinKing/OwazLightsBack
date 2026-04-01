from django.db import models

# Create your models here.
class UserCredentials(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Почты пользователей"
        verbose_name = "Почта пользователя"

    def __str__(self):
        return self.full_name