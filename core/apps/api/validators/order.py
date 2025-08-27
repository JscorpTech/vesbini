# from django.core.exceptions import ValidationError


class OrderValidator:
    def __init__(self): ...

    def __call__(self):
        return True


class ItemValidator:
    def __init__(self): ...

    def __call__(self):
        return True
