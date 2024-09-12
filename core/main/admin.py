from django.contrib import admin
from .models import Category, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
