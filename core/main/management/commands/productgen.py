import json
import random
from random import randint
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand

# Project imports
from main.models import (
    Category,
    Product,
    Order,
    OrderItem,
)  # Ensure correct import path


class Command(BaseCommand):
    help = "This command generates random data for Categories, Products, Orders, and OrderItems."

    json_data = """
      [
          {"color": "red", "size": "M"},
          {"color": "blue", "size": "L"},
          {"color": "green", "size": "S"},
          {"color": "yellow", "size": "XL"}
      ]
    """

    def random_datetime(self, start, end):
        time_delta = end - start
        random_seconds = random.randint(0, int(time_delta.total_seconds()))
        return start + timedelta(seconds=random_seconds)

    # Function to create random categories
    def create_categories(self, count=10):
        categories = []
        for i in range(count):
            category_title = get_random_string(10)
            category = Category.objects.create(title=category_title)
            categories.append(category)
            self.stdout.write(
                self.style.SUCCESS(f"Category '{category_title}' created.")
            )
        return categories

    # Function to create random products
    def create_products(self, categories, count=10):
        products = []
        data = json.loads(self.json_data)  # Load JSON attributes
        start_date = datetime(2022, 1, 1, 0, 0, 0)
        end_date = datetime(2024, 12, 31, 23, 59, 59)

        for i in range(count):
            product_category = random.choice(categories)
            product_name = get_random_string(8)
            product_description = get_random_string(50)
            product_stock = random.randint(1, 10)
            product_is_active = bool(random.randint(0, 1))
            product_attributes = random.choice(data)
            created_at = self.random_datetime(start_date, end_date)
            updated_at = self.random_datetime(created_at, end_date)
            product = Product.objects.create(
                category=product_category,
                name=product_name,
                description=product_description,
                stock=product_stock,
                is_active=product_is_active,
                attributes=product_attributes,
                created_at=created_at,
                updated_at=updated_at,
            )
            products.append(product)
            self.stdout.write(self.style.SUCCESS(f"Product '{product_name}' created."))
        return products

    # Function to create random orders (only one user is used)
    def create_orders(self, user, count=10):
        orders = []
        start_date = datetime(2022, 1, 1, 0, 0, 0)
        end_date = datetime(2024, 12, 31, 23, 59, 59)

        for i in range(count):
            order_status = random.choice(["PN", "SH", "DL"])
            created_at = self.random_datetime(start_date, end_date)
            order = Order.objects.create(
                user=user,
                status=order_status,
                created=created_at,
            )
            orders.append(order)
            self.stdout.write(
                self.style.SUCCESS(f"Order for user '{user.username}' created.")
            )
        return orders

    # Function to create random order items
    def create_order_items(self, orders, products, count=10):
        for i in range(count):
            order = random.choice(orders)
            product = random.choice(products)
            quantity = random.randint(1, 5)
            order_item = OrderItem.objects.create(
                order=order, product=product, quantity=quantity
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"OrderItem for Order '{order.id}' and Product '{product.name}' created."
                )
            )

    def handle(self, *args, **kwargs):
        # Get a single user from the database
        user = User.objects.first()  # Fetch only one user

        if not user:
            self.stdout.write(
                self.style.ERROR(
                    "No users found in the database. Please create at least one user first."
                )
            )
            return

        # Create 10 random categories
        categories = self.create_categories(10)

        # Create 10 random products
        products = self.create_products(categories, 10)

        # Create 10 random orders for the single user
        orders = self.create_orders(user, 10)

        # Create 10 random order items
        self.create_order_items(orders, products, 10)
