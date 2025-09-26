import logging

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from payme import Payme
from payme.views import PaymeWebHookAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import Response

from core.apps.api.models.order import OrderModel

payme = Payme(payme_id=settings.PAYME_ID)


class PaymeCallBackAPIView(PaymeWebHookAPIView):
    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction successfully performed for this params: {params} and performed_result: {result}")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")


@api_view(["GET"])
@permission_classes([AllowAny])
def generate_transaction_payme(request, order_id):
    logging.info(request.data)
    order = OrderModel.objects.filter(id=order_id).first()
    if order is None:
        return Response(data={"status": False, "data": {"detail": _("Order not found")}})
    paylink = payme.initializer.generate_pay_link(
        id=order_id,
        amount=order.payment_amount,
        return_url=settings.REDIRECT_LINK,
    )
    return Response(data={"status": True, "data": {"paylink": paylink}})
