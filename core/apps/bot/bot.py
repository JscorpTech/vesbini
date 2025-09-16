import logging

from telebot import TeleBot, custom_filters
from telebot.storage.redis_storage import StateRedisStorage

from config.env import env
from core.apps.bot.filters import MessageFilter, PageFilter
from core.apps.bot.middlewares import LocaleMiddleware

try:
    storage = StateRedisStorage(redis_url=env.str("REDIS_URL"))
    bot = TeleBot(
        token=env.str("BOT_TOKEN"),
        state_storage=storage,
        use_class_middlewares=True,
        parse_mode="HTML",
    )
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(MessageFilter())
    bot.add_custom_filter(PageFilter())
    bot.setup_middleware(LocaleMiddleware())
except Exception as e:
    logging.error("Bot variable yaratilmadi")
    logging.error(e)
