from django.urls import path

from .views import ClickWebhookAPIView

urlpatterns = [
    path("click/webhook/", ClickWebhookAPIView.as_view()),
]
