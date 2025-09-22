from telebot.types import Message

from core.apps.bot.bot import bot
from core.apps.bot.buttons import buttons
from core.apps.bot.services import get_message as _
from core.apps.bot.states.pages import Admin


@bot.message_handler(commands=["start"])
def start(msg: Message):
    bot.send_message(msg.chat.id, _("start_message"), reply_markup=buttons.home())


@bot.message_handler(is_admin=True, commands=["message"])
def message_handler(msg: Message):
    bot.set_state(msg.chat.id, Admin.message)
    bot.send_message(msg.chat.id, _("send_message"))


@bot.message_handler(is_admin=True, state=Admin.message)
def admin_send_message_handler(msg: Message):
    bot.send_message(msg.chat.id, "keldi")
