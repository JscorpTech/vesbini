from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.payment.models import HistoryModel
from core.apps.payment.serializers.history import (
    CreateHistorySerializer,
    ListHistorySerializer,
    RetrieveHistorySerializer,
)


@extend_schema(tags=["history"])
class HistoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    serializer_class = ListHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HistoryModel.objects.order_by("-id").filter(user=self.request.user).all()

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHistorySerializer,
        "retrieve": RetrieveHistorySerializer,
        "create": CreateHistorySerializer,
    }
