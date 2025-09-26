def add_balance(user, amount):
    profile = user.profile
    profile.balance += amount
    profile.save()


def subtract_balance(user, amount):
    profile = user.profile
    profile.balance -= amount
    profile.save()
