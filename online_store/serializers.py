from rest_framework import serializers
from .models import Category, Product, User, Rating, UserCart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            "count",
            "rate",
        ]


class ProductSerializer(serializers.ModelSerializer):
    rating = RatingSerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "category",
            "description",
            "image",
            "rating",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = [
            "id",
            "product",
            "quantity",
        ]


class UserCartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    items = CartItemSerializer(many=True)

    class Meta:
        model = UserCart
        fields = ["id", "user", "items", "created_at"]
