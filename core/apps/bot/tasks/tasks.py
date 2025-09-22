import time

from celery import shared_task

from core.apps.bot.bot import bot
from core.apps.bot.models.bot import BotUser


@shared_task
def send_message_task(message_id, from_chat_id):
    print("Foydalanuvchilarga xabar yuborilmoqda")
    for user in BotUser.objects.all():
        try:
            bot.copy_message(from_chat_id=from_chat_id, message_id=message_id, chat_id=user.chat_id)
        except Exception as e:
            print(e)
        time.sleep(1)
