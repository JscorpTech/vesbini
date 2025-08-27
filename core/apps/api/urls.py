from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.apps.api.views import BasketView, CategoryView, ColorView, OrderView, ProductView, SizeView, TagView

router = DefaultRouter()
router.register("product", ProductView, basename="product")
router.register("category", CategoryView, basename="category")
router.register("size", SizeView, basename="size")
router.register("color", ColorView, basename="color")
router.register("tag", TagView, basename="tag")
router.register("basket", BasketView, basename="basket")
router.register("order", OrderView, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]
