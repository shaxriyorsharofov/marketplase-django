from django.db import models
from users.models import CustomUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10000000, decimal_places=2)
    address = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductsImage(models.Model):
    image = models.ImageField(upload_to='products/')
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.products.title


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('Comment of' + self.author.username)
