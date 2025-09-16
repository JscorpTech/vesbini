from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

from core.apps.bot.services import get_message as _


def home():
    button = InlineKeyboardMarkup()
    button.add(InlineKeyboardButton(_("mini_app"), web_app=WebAppInfo(url="https://vesbini-latest.vercel.app/")))
    return button
