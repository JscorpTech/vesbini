from django.db import models

from core.apps.accounts.services import add_balance
from core.apps.accounts.services.balance import subtract_balance
from core.services.cashback import calc_cashback


def order_total_amount(order):
    amount = order.items.aggregate(total=models.Sum(models.F("amount") * models.F("count")))["total"]  # type: ignore
    if order.is_delivery:
        amount += order.delivery_method.price
    return amount


def confirm_order(order):
    from core.apps.api.tasks.moysklad import order_moysklad

    add_balance(order.user, calc_cashback(order))
    order_moysklad.delay(order.id)


def cancel_order(order):
    subtract_balance(order.user, calc_cashback(order))
