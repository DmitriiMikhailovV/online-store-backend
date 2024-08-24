from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from online_store.views import (
    CategoryViewSet,
    ProductViewSet,
    ProductDetailView,
    UserViewSet,
    RatingViewSet,
    UserCartViewSet,
)
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"users", UserViewSet)
router.register(r"rating", RatingViewSet)
router.register(r"user_cart", UserCartViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("products/<int:id>/", ProductDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
