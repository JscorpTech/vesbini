from telebot import custom_filters

from core.apps.bot.services import get_data
from core.apps.bot.services import get_message as _


class MessageFilter(custom_filters.AdvancedCustomFilter):
    key = "message"

    def check(self, message, data):
        if type(data) in [list, tuple]:
            for msg in data:
                if message.text == _(msg):
                    return True
            return False
        return message.text == _(data)


class PageFilter(custom_filters.AdvancedCustomFilter):
    key = "page"

    def check(self, message, pages):
        if type(pages) in [list, tuple]:
            for page in pages:
                if get_data(message.chat.id, "page") == page:
                    return True
            return False
        return get_data(message.chat.id, "page") == pages
