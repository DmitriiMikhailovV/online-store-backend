from rest_framework import serializers
from .models import Category, Product, User, Rating, UserCart, CartItem
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import base64


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation["image"] = base64.b64encode(instance.image).decode(
                "utf-8"
            )
        return representation

    def validate_image(self, value):
        if isinstance(value, str):
            return value.encode("utf-8")
        return value

    def create(self, validated_data):
        if "image" in validated_data:
            validated_data["image"] = validated_data["image"].read()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "image" in validated_data:
            validated_data["image"] = validated_data["image"].read()
        return super().update(instance, validated_data)


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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "A user with this username already exists."
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(RegisterSerializer, self).create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
        }

        return data
