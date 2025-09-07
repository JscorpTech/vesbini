from core.apps.api.models.moysklad import RetailShiftModel


def active_retailshift():
    queryset = RetailShiftModel.objects.filter(is_active=True).first()
    if queryset is None:
        return None
    return queryset.href
