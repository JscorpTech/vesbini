from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.apps.payment.views.payme import PaymeCallBackAPIView

from .views import ClickWebhookAPIView, HistoryView, generate_transaction_click, generate_transaction_payme

router = DefaultRouter()
router.register("history", HistoryView, basename="history")

urlpatterns = [
    path("", include(router.urls)),
    path("click/webhook/", ClickWebhookAPIView.as_view()),
    path("payme/webhook/", PaymeCallBackAPIView.as_view()),
    path("click/transaction/<int:order_id>", generate_transaction_click, name="click_transaction"),
    path("payme/transaction/<int:order_id>", generate_transaction_payme, name="payme_transaction"),
]
