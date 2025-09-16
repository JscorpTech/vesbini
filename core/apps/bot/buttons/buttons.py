from core.apps.bot.services import get_message as _
from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def home():
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(KeyboardButton(_("example")), KeyboardButton(_("example")))
    return button
