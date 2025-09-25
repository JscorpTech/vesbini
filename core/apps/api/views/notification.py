from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from core.apps.api.models import UserNotificationModel
from core.apps.api.serializers.notification import (
    CreateUsernotificationSerializer,
    ListUsernotificationSerializer,
    RetrieveUsernotificationSerializer,
)

# @extend_schema(tags=["notification"])
# class NotificationView(BaseViewSetMixin, ReadOnlyModelViewSet):
#     queryset = NotificationModel.objects.all()
#     serializer_class = ListNotificationSerializer
#     permission_classes = [AllowAny]
#
#     action_permission_classes = {}
#     action_serializer_class = {
#         "list": ListNotificationSerializer,
#         "retrieve": RetrieveNotificationSerializer,
#         "create": CreateNotificationSerializer,
#     }


@extend_schema(tags=["usernotification"])
class UserNotificationView(BaseViewSetMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = ListUsernotificationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):  # type:ignore
        return UserNotificationModel.objects.order_by("-id").filter(user=self.request.user)

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListUsernotificationSerializer,
        "retrieve": RetrieveUsernotificationSerializer,
        "create": CreateUsernotificationSerializer,
    }

    @action(methods=["POST"], detail=True, url_path="read", url_name="read")
    def read(self, request, pk=None):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        return self.retrieve(request, pk)
