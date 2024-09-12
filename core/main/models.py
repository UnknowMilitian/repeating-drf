from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=255)

    def __str__(self):
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(
        Category, verbose_name=_("blog"), on_delete=models.CASCADE
    )
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Description"))

    def __str__(self):
        return self.title
