from rest_framework import viewsets, generics
from .models import Category, Product, Rating, User, UserCart
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    RatingSerializer,
    UserSerializer,
    UserCartSerializer,
)
from django.http import JsonResponse


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCartViewSet(viewsets.ModelViewSet):
    queryset = UserCart.objects.all()
    serializer_class = UserCartSerializer
