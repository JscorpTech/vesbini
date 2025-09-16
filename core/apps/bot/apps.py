from django.apps import AppConfig


class ModuleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.bot"

    def ready(self) -> None:
        import core.apps.bot.signals
