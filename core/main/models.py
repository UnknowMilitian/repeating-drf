from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=250)

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
    attributes = models.JSONField(_("Attributes"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = {"PN": "Pending", "SH": "Shipped", "DL": "Delivered"}

    user = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=10, choices=STATUS, default="PN")
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    quantity = models.IntegerField(_("Quantity"), default=0)

    def __str__(self):
        return f"Order: {self.order}, Product: {self.product.name}, Quantity: {self.quantity}"
