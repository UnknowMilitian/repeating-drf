from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    email = None
    username = None

    phone = models.CharField(_("Phone"), max_length=15, unique=True)
    full_name = models.CharField(_("Full name"), max_length=255, null=True, blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()


class Token(models.Model):
    token = models.CharField(_("Token"), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def __str__(self):
        return f"Token for user {self.user}"


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
