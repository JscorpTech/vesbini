from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core.apps.api.models import PromocodeModel
from core.apps.api.serializers.promocode.promocode import CheckPromocodeSerializer


@extend_schema(tags=["promocode"])
class PromocodeView(BaseViewSetMixin, GenericViewSet):
    queryset = PromocodeModel.objects.all()
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "validate": CheckPromocodeSerializer,
    }

    @extend_schema(
        summary="Promocode mavjud ekanligini tekshirish",
        responses={
            200: CheckPromocodeSerializer,
            400: OpenApiResponse(
                response={
                    "type": "object",
                    "properties": {
                        "status": {"type": "bool", "example": False},
                        "data": {
                            "type": "object",
                            "properties": {"detail": {"type": "string", "example": "Promocode is expired"}},
                        },
                    },
                }
            ),
        },
    )
    @action(methods=["post"], detail=False, url_name="validate", url_path="validate")
    def validate(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, code=request.data.get("code"))
        if obj.quantity == 0:
            raise ValidationError(detail={"detail": "Promocode is expired"})
        ser = self.get_serializer(instance=obj)
        return Response(data=ser.data)
