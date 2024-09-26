from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# App imports
from .models import Item
from .authenticate import BaseAuthentication
from .serializers import ItemSerializer, UserRegistrationSerializer, UserLoginSerializer


class ItemListAPIVIew(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Registration Views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class LoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
