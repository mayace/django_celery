import uuid
from django.db import models

from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    id = models.UUIDField(
        _("Id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    text = models.TextField(_("Text"))
    checked = models.BooleanField(
        _("Checked"),
        default=False,
    )

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        return self.name
