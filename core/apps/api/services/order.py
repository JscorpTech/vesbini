from django.db import models


def order_total_amount(order):
    amount = order.items.aggregate(total=models.Sum(models.F("amount") * models.F("count")))["total"]  # type: ignore
    if order.is_delivery:
        amount += order.delivery_method.price
    return amount
