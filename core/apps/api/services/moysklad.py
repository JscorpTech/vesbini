from core import services
from core.apps.api.models.moysklad import RetailShiftModel, StoreModel
from core.services.moysklad import MoySklad


def active_retailshift():
    queryset = RetailShiftModel.objects.filter(is_active=True).first()
    if queryset is None:
        return None
    return queryset.href


def default_store():
    queryset = StoreModel.objects.filter(default=True).first()
    if queryset is None:
        return None
    return queryset.href


def counterparty(user):
    service = MoySklad()
    if user.href is None:
        href = service.counterparty(user.first_name, user.phone)
        user.href = href
        user.save()
    return user.href
