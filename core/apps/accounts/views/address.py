from django_core.mixins import BaseViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import DistrictModel, RegionModel
from core.apps.accounts.serializers.address import (
    CreateDistrictSerializer,
    CreateRegionSerializer,
    ListDistrictSerializer,
    ListRegionSerializer,
    RetrieveDistrictSerializer,
    RetrieveRegionSerializer,
)


@extend_schema(tags=["region"])
class RegionView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = RegionModel.objects.all()
    serializer_class = ListRegionSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListRegionSerializer,
        "retrieve": RetrieveRegionSerializer,
        "create": CreateRegionSerializer,
    }


@extend_schema(tags=["district"])
class DistrictView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = DistrictModel.objects.all()
    serializer_class = ListDistrictSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["region"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDistrictSerializer,
        "retrieve": RetrieveDistrictSerializer,
        "create": CreateDistrictSerializer,
    }
