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
    RegisterView,
)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"users", UserViewSet)
router.register(r"rating", RatingViewSet)
router.register(r"user_cart", UserCartViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("products/<int:id>/", ProductDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("register/", RegisterView.as_view(), name="register"),
    ]
