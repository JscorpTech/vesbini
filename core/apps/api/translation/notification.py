from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import NotificationModel, UserNotificationModel


@register(NotificationModel)
class NotificationTranslation(TranslationOptions):
    fields = []


@register(UserNotificationModel)
class UsernotificationTranslation(TranslationOptions):
    fields = []
