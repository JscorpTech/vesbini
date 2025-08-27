from django.db import models


def order_total_amount(order):
    return order.items.aggregate(total=models.Sum(models.F("variant__amount") * models.F("count")))["total"]  # type: ignore
