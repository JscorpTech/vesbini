from core.apps.api.models.promocode import PromocodeModel


def validate_promocode(promocode: str):
    obj = PromocodeModel.objects.filter(code=promocode).first()
    if obj is None:
        return False
    if obj.quantity == 0:
        return False
    return True


def subtract_promocode(promocode):
    if promocode is None:
        return
    if promocode.quantity == -1:
        return
    if promocode.quantity == 0:
        raise Exception("Promocode not found")
    promocode.quantity -= 1
    promocode.save()
