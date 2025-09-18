from django_filters import rest_framework as filters

from core.apps.api.models import FeedbackModel


class FeedbackFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = FeedbackModel
        fields = [
            "name",
        ]
