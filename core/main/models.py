from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Settings(SingletonModel):
    hours = models.IntegerField()
    days = models.CharField(max_length=30)


class User(AbstractUser):
    phone = PhoneNumberField(_("Phone"), unique=True)

    # Add related_name to resolve clashes with auth.User
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_user_set",  # Changed related name
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_user_permissions_set",  # Changed related name
    )

    def __str__(self):
        return self.phone


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=250)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product"
    )
    name = models.CharField(_("Name"), max_length=250)
    description = models.TextField(_("Description"), blank=True)
    stock = models.IntegerField(_("Stock"), default=1)
    is_active = models.BooleanField(_("Is active"), default=False)
    price = models.IntegerField(_("Price"), default=1)
    attributes = models.JSONField(_("Attributes"))
    created_at = models.DateTimeField(_("Created at"), auto_now=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = {"PN": "Pending", "SH": "Shipped", "DL": "Delivered"}

    user = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=10, choices=STATUS, default="PN")
    created = models.DateTimeField(_("Created"), auto_now=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="Order",
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    quantity = models.IntegerField(_("Quantity"), default=0)

    class Meta:
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItems")

    def __str__(self):
        return f"Order: {self.order}, Product: {self.product.name}, Quantity: {self.quantity}"


class TestingImageDisplaying(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    image = models.ImageField(_("Image"), upload_to="images/")

    def __str__(self):
        return self.title
