from typing import Any

from django.core.management import BaseCommand

from core.services.moysklad import MoySklad


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        service = MoySklad()
