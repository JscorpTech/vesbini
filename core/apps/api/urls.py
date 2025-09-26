from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.apps.api.views import BasketView, CategoryView, ColorView, OrderView, ProductView, SizeView, TagView
from core.apps.api.views.delivery import DeliveryMethodView
from core.apps.api.views.notification import UserNotificationView

from .views import FeedbackView, PromocodeView

router = DefaultRouter()
router.register("promocode", PromocodeView, basename="promocode")
router.register("feedback", FeedbackView, basename="feedback")
router.register("product", ProductView, basename="product")
router.register("category", CategoryView, basename="category")
router.register("size", SizeView, basename="size")
router.register("color", ColorView, basename="color")
router.register("tag", TagView, basename="tag")
router.register("basket", BasketView, basename="basket")
router.register("order", OrderView, basename="order")
router.register("notification", UserNotificationView, basename="notification")
router.register("delivery-method", DeliveryMethodView, basename="delivery-method")
urlpatterns = [path("", include(router.urls))]
