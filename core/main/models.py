from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    description = models.TextField(_("Description"), null=True, blank=True)

    def __str__(self):
        return f"Title {title}"
