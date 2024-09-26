from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# App imports
from .models import Item
from .authentication import CustomBasicAuthentication
from .serializers import (
    ItemSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    RegisterSerializer,
)


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomBasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "message": "Пользователь успешно зарегистрирован!",
            },
            status=status.HTTP_201_CREATED,
        )
