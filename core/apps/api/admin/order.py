from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from core.apps.api.models import ItemModel, OrderModel
from core.apps.api.services.order import order_total_amount


class ItemInline(TabularInline):
    model = ItemModel
    extra = 0
    tab = True

    def get_readonly_fields(self, request, obj):
        return ["product", "count", "variant", "amount"]

    def has_add_permission(self, request, obj) -> bool:
        return False

    def has_delete_permission(self, request, obj) -> bool:
        return False


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    inlines = [ItemInline]
    list_display = (
        "id",
        "__str__",
        "user__first_name",
        "user__phone",
    )

    readonly_fields = ["amount"]

    def amount(self, obj):
        return order_total_amount(obj)

    amount.short_desctiption = "Amount"


@admin.register(ItemModel)
class ItemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
