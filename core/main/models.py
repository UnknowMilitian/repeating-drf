from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    email = None
    username = None

    phone = models.CharField(_("Phone"), max_length=20, unique=True)
    full_name = models.CharField(_("Full name"), max_length=255, null=True, blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone


class Blog(models.Model):
    title = models.CharField(_("Title"), max_length=20)

    def __str__(self):
        return self.title
