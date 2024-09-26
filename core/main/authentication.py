import base64
from rest_framework.authentication import BaseAuthentication

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class BasicAuthentication(BaseAuthentication):
    def get_header(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if isinstance(auth_header, str):
            auth_header = auth_header.encode()
        return auth_header

    def authenticate(self, request):
        auth_header = self.get_header(request)

        if not auth_header:
            return None

        auth_header = auth_header.split()

        if len(auth_header) != 2 or auth_header[0].lower() != b"basic":
            return None

        auth_header = base64.b64encode(auth_header[1]).decode()
        phone, password = auth_header.split(":")

        user = authenticate(request=request, phone=phone, password=password)

        if user is None:
            return None

        return (user, None)
