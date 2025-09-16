from core.apps.bot.views.bot import BotView
from django.urls import path

urlpatterns = [
    path("webhook/", BotView.as_view(), name="bot"),
]
