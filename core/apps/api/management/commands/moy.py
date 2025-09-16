from typing import Any

from django.core.management import BaseCommand

from core.services.moysklad import MoySklad


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        service = MoySklad()
        print(
            list(
                service.stok(
                    hrefs=["https://api.moysklad.ru/api/remap/1.2/entity/bundle/0b76b32e-8629-11f0-0a80-03c300348332"],
                    kind="bundle",
                )
            )
        )
        print(
            list(
                service.stok(
                    hrefs=["https://api.moysklad.ru/api/remap/1.2/entity/product/3d33ddaf-5e56-11f0-0a80-01f4001b81ae"],
                    kind="product",
                )
            )
        )
