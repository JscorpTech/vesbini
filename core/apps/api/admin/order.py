from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.filters.admin import BooleanRadioFilter, ChoicesDropdownFilter, FieldTextFilter
from unfold.decorators import display

from core.apps.api.models import ItemModel, OrderModel
from core.apps.api.services.order import order_total_amount


class ItemInline(StackedInline):
    model = ItemModel
    extra = 0

    def get_readonly_fields(self, request, obj):
        return ["product", "count", "variant", "amount"]

    def has_add_permission(self, request, obj) -> bool:
        return False

    def has_delete_permission(self, request, obj) -> bool:
        return False


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    inlines = [ItemInline]
    list_filter_submit = True
    autocomplete_fields = ["user"]
    list_filter = (
        ("user__phone", FieldTextFilter),
        ("user__first_name", FieldTextFilter),
        ("status", ChoicesDropdownFilter),
        ("payment_status", BooleanRadioFilter),
    )
    list_display = ("id", "user__phone", "user__first_name", "_payment_status", "_status", "_amount", "created_at")

    readonly_fields = ["amount", "href"]

    def amount(self, obj):
        return "{:,.2f} so'm".format(order_total_amount(obj))

    amount.short_desctiption = "Amount"

    @display(
        ordering="status",
        label={
            _("new"): "info",
            _("delivering"): "warning",
            _("done"): "success",
            _("canceled"): "danger",
        },
        description=_("status"),
    )
    def _status(self, obj):
        return _(obj.status)

    @display(description=_("payment status"), boolean=True)
    def _payment_status(self, obj):
        return obj.payment_status

    @display(description=_("amount"), label=True)
    def _amount(self, obj):
        return self.amount(obj)


@admin.register(ItemModel)
class ItemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
