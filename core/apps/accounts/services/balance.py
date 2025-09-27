from core.apps.payment.models.history import HistoryModel


def add_balance(user, amount):
    profile = user.profile
    profile.balance += amount
    profile.save()
    HistoryModel.objects.create(user=user, amount=amount, type="income")


def subtract_balance(user, amount):
    profile = user.profile
    profile.balance -= amount
    profile.save()
    HistoryModel.objects.create(user=user, amount=amount, type="outcome")
