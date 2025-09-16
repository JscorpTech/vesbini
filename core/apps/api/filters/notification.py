from django_filters import rest_framework as filters

from core.apps.api.models import NotificationModel, UserNotificationModel


class NotificationFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = NotificationModel
        fields = [
            "name",
        ]


class UsernotificationFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = UserNotificationModel
        fields = [
            "name",
        ]
