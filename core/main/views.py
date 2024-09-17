import uuid
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import (
    BaseAuthentication as RetriveBasicAuthentication,
)
from rest_framework.views import APIView

from .models import User, Blog
from .serializers import (
    UserDetailSerializer,
    PhoneAndPasswordSerializer,
    BlogSerializer,
)
from .authentication import BasicAuthentication
from .utils import create_basic_authentication_header, generate_code

from django.contrib.auth import authenticate
from datetime import datetime
from django.core.cache import cache


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class Login(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, _ = User.objects.get_or_create(
            phone=serializer.validated_data["phone"], username=uuid.uuid4()
        )


# class LoginOtp(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserDetailSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         code = generate_code()
#         if cache.keys(f"otp_{serializer.validated_data['phone']}"):
#             return Response({"date": "sms_sent"})
