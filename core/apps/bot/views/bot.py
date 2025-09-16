from core.apps.bot import handlers  # noqa
from core.apps.bot.bot import bot
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from telebot.types import Update


class BotView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(status=204)

    def post(self, request):
        update = Update.de_json(request.body.decode("utf-8"))
        bot.process_new_updates([update])
        return Response(data={"detail": "OK"})
