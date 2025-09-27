from django.db import models

from core.apps.accounts.services import add_balance
from core.apps.accounts.services.balance import subtract_balance
from core.apps.api.enums.promocode import PromocodeTypeEnum
from core.apps.api.models.promocode import PromocodeModel
from core.services.cashback import calc_cashback


def order_total_amount(order) -> int:
    amount = order.items.aggregate(total=models.Sum(models.F("amount") * models.F("count")))["total"]  # type: ignore
    if order.is_delivery:
        amount += order.delivery_method.price
    if amount is None:
        return 0
    return amount


def order_total_amount_promocode(order):
    amount = order_total_amount(order)
    return calc_promocode_amount(amount, order.promocode)


def calc_promocode_amount(amount, promocode):
    return amount - calc_promocode_discount(amount, promocode)


def calc_promocode_discount(amount, code):
    if isinstance(code, str):
        promocode = PromocodeModel.objects.filter(code=code).first()
    else:
        promocode = code
    if promocode is None:
        return 0
    if promocode.promo_type == PromocodeTypeEnum.FIXED.value:
        return promocode.discount
    if promocode.promo_type == PromocodeTypeEnum.PERCENTAGE.value:
        return amount * promocode.discount / 100
    return 0


def confirm_order(order, cashback=True):
    from core.apps.api.tasks.moysklad import order_moysklad

    if cashback:
        add_balance(order.user, calc_cashback(order))
    order_moysklad.delay(order.id)


def cancel_order(order):
    subtract_balance(order.user, calc_cashback(order))
