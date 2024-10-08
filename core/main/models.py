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
    price = models.IntegerField(_("Price"), default=1)
    attributes = models.JSONField(_("Attributes"))
    created_at = models.DateTimeField(_("Created at"), auto_now=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = {"PN": "Pending", "SH": "Shipped", "DL": "Delivered"}

    user = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=10, choices=STATUS, default="PN")
    created = models.DateTimeField(_("Created"), auto_now=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items", verbose_name="Order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.IntegerField(_("Quantity"), default=0)

    def __str__(self):
        return f"Order: {self.order}, Product: {self.product.name}, Quantity: {self.quantity}"


# orm_1 = User.objects.annotate(
#     order_num=Count("order", distinct=True),
#     order_sum=Sum("order__orderitem__product__price"),
#     unique_prod=Count("order__orderitem__product", distinct=True),
# )


# orm_2 // Qila olmadim


# orm_3 = 

# from django.db.models import Q

# def filter_products_by_json(json_data):
#     filter_conditions = Q()
#     for key, value in json_data.items():
#         filter_conditions &= Q(attributes__contains={key: value})

#     products = Product.objects.filter(filter_conditions)
#     return products

# # Пример использования
# json_data = {'color': 'red', 'size': 'L'}
# filtered_products = filter_products_by_json(json_data)


# orm_4  = Order.objects.prefetch_related('order_items__product__category')


# orm_5 = Qila olmadim

# orm_6 = 
# from django.db.models import Count, Sum
# from django.db.models.functions import TruncMonth
# from django.utils import timezone
# from datetime import timedelta

# # Calculate the date for 12 months ago
# one_year_ago = timezone.now() - timedelta(days=365)

# # Query to get the number of orders and total sales for each month
# monthly_report = (
#     Order.objects.filter(created__gte=one_year_ago)  # Filter orders from the last year
#     .annotate(month=TruncMonth('created'))  # Group by month
#     .values('month')  # Select the month
#     .annotate(
#         total_orders=Count('id'),  # Count the number of orders
#         total_sales=Sum(F('order_items__product__price') * F('order_items__quantity'))  # Sum total sales
#     )
#     .order_by('month')  # Order the result by month
# )
