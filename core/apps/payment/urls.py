from django.urls import path

from core.apps.payment.views.payme import PaymeCallBackAPIView

from .views import ClickWebhookAPIView, generate_transaction_click, generate_transaction_payme

urlpatterns = [
    path("click/webhook/", ClickWebhookAPIView.as_view()),
    path("payme/webhook/", PaymeCallBackAPIView.as_view()),
    path("click/transaction/<int:order_id>", generate_transaction_click, name="click_transaction"),
    path("payme/transaction/<int:order_id>", generate_transaction_payme, name="payme_transaction"),
]
