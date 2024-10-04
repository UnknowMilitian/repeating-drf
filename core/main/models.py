from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Item(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    description = models.TextField(_("Description"), null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to="item")
    resized_image = ResizedImageField(
        size=[500, 300],
        upload_to="item",
        crop=["middle", "center"],
        force_format="PNG",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Title {self.title}"
