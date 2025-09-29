from django_core.mixins import BaseViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from core.apps.api.serializers.product import (
    CreateBasketSerializer,
    CreateCategorySerializer,
    CreateColorSerializer,
    CreateProductSerializer,
    CreateSizeSerializer,
    CreateTagSerializer,
    ListBasketSerializer,
    ListCategorySerializer,
    ListColorSerializer,
    ListProductSerializer,
    ListSizeSerializer,
    ListTagSerializer,
    RetrieveBasketSerializer,
    RetrieveCategorySerializer,
    RetrieveColorSerializer,
    RetrieveProductSerializer,
    RetrieveSizeSerializer,
    RetrieveTagSerializer,
)
from core.apps.api.serializers.product.basket import UpdateBasketSerializer


@extend_schema(tags=["product"])
class ProductView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["colors", "sizes", "amount", "categories", "tags"]
    search_fields = ["title", "desc"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProductSerializer,
        "retrieve": RetrieveProductSerializer,
        "create": CreateProductSerializer,
    }


@extend_schema(tags=["tag"])
class TagView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = ListTagSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTagSerializer,
        "retrieve": RetrieveTagSerializer,
        "create": CreateTagSerializer,
    }


@extend_schema(tags=["category"])
class CategoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCategorySerializer,
        "retrieve": RetrieveCategorySerializer,
        "create": CreateCategorySerializer,
    }


@extend_schema(tags=["color"])
class ColorView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ColorModel.objects.all()
    serializer_class = ListColorSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListColorSerializer,
        "retrieve": RetrieveColorSerializer,
        "create": CreateColorSerializer,
    }


@extend_schema(tags=["size"])
class SizeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = SizeModel.objects.all()
    serializer_class = ListSizeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSizeSerializer,
        "retrieve": RetrieveSizeSerializer,
        "create": CreateSizeSerializer,
    }


@extend_schema(tags=["basket"])
class BasketView(BaseViewSetMixin, ModelViewSet):
    serializer_class = ListBasketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):  # type:ignore
        return BasketModel.objects.order_by("-id").filter(user=self.request.user).all()

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBasketSerializer,
        "retrieve": RetrieveBasketSerializer,
        "create": CreateBasketSerializer,
        "update": UpdateBasketSerializer,
        "partial_update": UpdateBasketSerializer,
    }
