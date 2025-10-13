# type: ignore
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from core.apps.api.models.product import ProductModel, ProductVariantModel
from core.apps.api.services.order import order_total_amount, order_total_amount_promocode

User = get_user_model()


class OrderModel(AbstractBaseModel):
    STATUS = (
        ("new", _("new")),
        ("delivering", _("delivering")),
        ("done", _("done")),
        ("canceled", _("canceled")),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(verbose_name=_("status"), max_length=255, choices=STATUS, default="new")
    payment_status = models.BooleanField(_("payment status"), default=False)
    delivery_method = models.ForeignKey("DeliveryMethodModel", on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(_("delivery address"), null=True, blank=True)
    is_delivery = models.BooleanField(_("is delivery"), default=False)
    href = models.CharField(_("href"), max_length=500, null=True, blank=True)
    promocode = models.ForeignKey(
        "PromocodeModel", verbose_name=_("promocode"), on_delete=models.SET_NULL, null=True, blank=True
    )
    use_cashback = models.BigIntegerField(_("use cashback amount"), default=0)
    promocode_discount = models.BigIntegerField(_("promocode discount"), default=0)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._payment_status = self.payment_status

    def clean(self) -> None:
        if self.is_delivery and self.delivery_method is None:
            raise ValidationError({"delivery_method": _("Delivery method field is required")})

    @property
    def amount(self):
        return order_total_amount_promocode(self)

    @property
    def orginal_amount(self):
        return order_total_amount(self)

    @property
    def payment_amount(self):
        return self.amount - self.use_cashback

    def __str__(self):
        return f"{self.pk} - {self.user.first_name} - {self.user.phone}"

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            user=User._create_fake(),
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")


class ItemModel(AbstractBaseModel):
    order = models.ForeignKey("OrderModel", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("ProductModel", on_delete=models.SET_NULL, null=True, related_name="items")
    count = models.BigIntegerField(_("count"), default=1)
    variant = models.ForeignKey("ProductVariantModel", on_delete=models.SET_NULL, null=True, related_name="items")
    amount = models.BigIntegerField(_("amount"), default=0)
    store = models.ForeignKey("StoreModel", verbose_name=_("sklad"), on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            order=OrderModel._create_fake(),
            product=ProductModel._create_fake(),
            count=10,
            variant=ProductVariantModel._create_fake(),
            amount=1000,
        )

    class Meta:
        db_table = "item"
        verbose_name = _("ItemModel")
        verbose_name_plural = _("ItemModels")
