from telebot.types import Message

from core.apps.bot.bot import bot
from core.apps.bot.services import get_message as _


@bot.message_handler(commands=["start"])
def start(msg: Message):
    bot.send_message(msg.chat.id, _("Assalomu Alaykum botga hush kelibsiz!!!"))
