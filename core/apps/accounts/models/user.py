from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from ..choices import RoleChoice
from ..managers import UserManager


class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.USER,
    )

    # address
    country = models.ForeignKey("CountryModel", on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey("RegionModel", on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = "phone"
    objects = UserManager()  # type: ignore

    @classmethod
    def _create_fake(cls):
        user = cls.objects.filter(phone="999999999").first()
        if user is not None:
            return user
        return cls.objects.create_user("999999999", password="nnnnnnn")

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.phone)


class Profile(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    qrcode = models.ImageField(_("qrcode"), upload_to="qrcode", null=True, blank=True)
    balance = models.BigIntegerField(default=0)
