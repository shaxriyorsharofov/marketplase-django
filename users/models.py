from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=17)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    tg_username = models.CharField(max_length=50)

    def __str__(self):
        return str(self.username)


class Saved(models.Model):
    products = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str('Saved of' + self.author.username)