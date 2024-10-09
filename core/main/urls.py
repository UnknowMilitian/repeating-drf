from django.urls import path
from .views import (
    UserListAPIView,
    CategoryListAPIView,
    ProductListAPIView,
    OrderListAPIView,
    OrderItemListAPIView,
)

urlpatterns = [
    path("user-list", UserListAPIView.as_view(), name="user-list"),
    path("category-list", CategoryListAPIView.as_view(), name="category-list"),
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
    path("order-list", OrderListAPIView.as_view(), name="order-list"),
    path("orderitem-list", OrderItemListAPIView.as_view(), name="orderitem-list"),
]
