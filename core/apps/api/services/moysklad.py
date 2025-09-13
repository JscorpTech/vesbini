from core.apps.api.models.moysklad import RetailShiftModel, StoreModel


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
