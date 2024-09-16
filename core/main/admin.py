from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Token, Category, Blog


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": ("password",),
            },
        ),
        (_("Personal info"), {"fields"}, ("phone", "full_name")),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        None,
        {"classes": ("wide",), "fields": ("usable_password", "password1", "password2")},
    )

    list_display = ("email", "full_name", "is_staff")
    search_fields = ("full_name", "email")
    ordering = ("full_name",)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
