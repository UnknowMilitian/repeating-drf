from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# App imports
# from .authentication import CustomBasicAuthentication
from .serializers import (
    # Main Serializers
    UserSerializer,
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer,
    # Registration Serializers
    # UserRegistrationSerializer,
    # UserLoginSerializer,
    # RegisterSerializer,
)
from .models import User, Category, Product, Order, OrderItem


# Main views
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "is_active",
    ]
    search_fields = ["name", "price"]


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemListAPIView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()

#         return Response(
#             {
#                 "user": {
#                     "username": user.username,
#                     "email": user.email,
#                     "first_name": user.first_name,
#                     "last_name": user.last_name,
#                 },
#                 "message": "Пользователь успешно зарегистрирован!",
#             },
#             status=status.HTTP_201_CREATED,
#         )
