from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Order, OrderItem


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    field = "title"


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description", "attributes")


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    field = "status"
