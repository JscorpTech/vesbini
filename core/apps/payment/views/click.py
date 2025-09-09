import logging

from click_up import ClickUp
from click_up.views import ClickWebhook
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import Response

from core.apps.api.models.order import OrderModel

click_up = ClickUp(service_id=settings.CLICK_SERVICE_ID, merchant_id=settings.CLICK_MERCHANT_ID)


class ClickWebhookAPIView(ClickWebhook):
    permission_classes = [AllowAny]

    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        order: OrderModel = OrderModel.objects.filter(pk=params.merchant_trans_id).first()  # type: ignore
        order.payment_status = True
        order.save()

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        print(f"payment cancelled params: {params}")


@api_view(["GET"])
@permission_classes([AllowAny])
def generate_transaction_click(request, order_id):
    logging.info(request.data)
    order = OrderModel.objects.filter(id=order_id).first()
    if order is None:
        return Response(data={"status": False, "data": {"detail": _("Order not found")}})
    paylink = click_up.initializer.generate_pay_link(
        id=order_id,
        amount=order.amount,
        return_url=settings.REDIRECT_LINK,
    )
    return Response(data={"status": True, "data": {"paylink": paylink}})
