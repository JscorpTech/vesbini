from django.urls import path

from .views import ClickWebhookAPIView, generate_transaction_click

urlpatterns = [
    path("click/webhook/", ClickWebhookAPIView.as_view()),
    path("click/transaction/<int:order_id>", generate_transaction_click, name="click_transaction"),
]
