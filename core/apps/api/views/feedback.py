from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import FeedbackModel
from core.apps.api.serializers.feedback import (
    CreateFeedbackSerializer,
    ListFeedbackSerializer,
    RetrieveFeedbackSerializer,
)


@extend_schema(tags=["feedback"])
class FeedbackView(BaseViewSetMixin, ModelViewSet):
    serializer_class = ListFeedbackSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListFeedbackSerializer,
        "retrieve": RetrieveFeedbackSerializer,
        "create": CreateFeedbackSerializer,
    }

    def get_queryset(self):
        return FeedbackModel.objects.order_by("-id").filter(user=self.request.user).all()
