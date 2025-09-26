from django.db import models
from django.utils.translation import gettext_lazy as _


class PromocodeTypeEnum(models.TextChoices):
    FIXED = "fixed", _("Fixed")
    PERCENTAGE = "percentage", _("Percentage")
