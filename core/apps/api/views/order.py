from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from httpx import request
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from core.apps.api.models import ItemModel, OrderModel
from core.apps.api.serializers.order import (
    CreateItemSerializer,
    CreateOrderSerializer,
    ListItemSerializer,
    ListOrderSerializer,
    RetrieveItemSerializer,
    RetrieveOrderSerializer,
)


@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ModelViewSet):
    serializer_class = ListOrderSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
    }

    def get_queryset(self):  # type:ignore
        return OrderModel.objects.order_by("-id").filter(user=self.request.user).all()


@extend_schema(tags=["item"])
class ItemView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ListItemSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListItemSerializer,
        "retrieve": RetrieveItemSerializer,
        "create": CreateItemSerializer,
    }
