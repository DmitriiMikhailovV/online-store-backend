from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    count = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return f"{self.rate} ({self.count} ratings)"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    description = models.TextField()
    image = models.BinaryField()
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class UserCart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="carts"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} cart created at {self.created_at}"


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    user_cart = models.ForeignKey(
        UserCart, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_items"
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.title} - {self.quantity} pcs"
