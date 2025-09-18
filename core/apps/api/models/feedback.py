from typing import Any

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

User = get_user_model()


class FeedbackModel(AbstractBaseModel):
    message = models.TextField(_("message"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(_("answer"), null=True, blank=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._answer = self.answer

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            message="test",
            user=User._create_fake(),
            answer="salom",
        )

    class Meta:
        db_table = "feedback"
        verbose_name = _("FeedbackModel")
        verbose_name_plural = _("FeedbackModels")
