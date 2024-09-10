from django.contrib import admin
from .models import Category, Women


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    pass
