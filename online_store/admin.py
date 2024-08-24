from django.contrib import admin
from .models import Category, Rating, Product, User, UserCart, CartItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("rate", "count")
    search_fields = ("rate",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")
    list_filter = ("category",)
    search_fields = ("title", "description")
    raw_id_fields = ("rating",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email")


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    raw_id_fields = ("user",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user_cart", "product", "quantity")
    raw_id_fields = ("user_cart", "product")
    list_filter = ("user_cart", "product")
    search_fields = ("product__title",)
