from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import DeliveryMethodModel
from core.apps.api.serializers.delivery import (
    CreateDeliveryMethodSerializer,
    ListDeliveryMethodSerializer,
    RetrieveDeliveryMethodSerializer,
)


@extend_schema(tags=["deliverymethod"])
class DeliveryMethodView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = DeliveryMethodModel.objects.all()
    serializer_class = ListDeliveryMethodSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDeliveryMethodSerializer,
        "retrieve": RetrieveDeliveryMethodSerializer,
        "create": CreateDeliveryMethodSerializer,
    }
