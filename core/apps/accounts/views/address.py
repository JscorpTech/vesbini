from django_core.mixins import BaseViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import CountryModel, RegionModel
from core.apps.accounts.serializers.address import (
    CreateCountrySerializer,
    CreateRegionSerializer,
    ListCountrySerializer,
    ListRegionSerializer,
    RetrieveCountrySerializer,
    RetrieveRegionSerializer,
)


@extend_schema(tags=["country"])
class CountryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = ListCountrySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCountrySerializer,
        "retrieve": RetrieveCountrySerializer,
        "create": CreateCountrySerializer,
    }


@extend_schema(tags=["region"])
class RegionView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = RegionModel.objects.all()
    serializer_class = ListRegionSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListRegionSerializer,
        "retrieve": RetrieveRegionSerializer,
        "create": CreateRegionSerializer,
    }
