from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import (
    User,
    Settings,
    Category,
    Product,
    Order,
    OrderItem,
    TestingImageDisplaying,
)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, AuthUserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(TestingImageDisplaying)
class TestingImageDisplayingAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:25px; max-height:25px"/>'.format(
                obj.image.url
            )
        )

    list_display = ["image_tag", "title"]
