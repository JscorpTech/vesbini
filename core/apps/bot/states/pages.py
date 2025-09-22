from telebot.handler_backends import State, StatesGroup


class Admin(StatesGroup):
    message = State()
