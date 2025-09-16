from django.utils import translation
from telebot.handler_backends import BaseMiddleware
from telebot.types import Message

from core.apps.bot.services import get_or_create_user


class LocaleMiddleware(BaseMiddleware):

    def __init__(self):
        self.update_types = ["message"]

    def pre_process(self, msg: Message, data):
        user, _ = get_or_create_user(msg.chat.id)
        translation.activate(user.lang)
