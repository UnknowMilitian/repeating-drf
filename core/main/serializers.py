from rest_framework import serializers
from rest_framework import exceptions
from .models import User, Blog


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "phone", "full_name", "is_staff", "is_superuser")


class PhoneAndPasswordSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255)

    def validate_password(self, value):
        if len(value) < 8:
            raise exceptions.ValidationError(
                "Password must be at least 8 characters long"
            )
        return value

    def validate(self, attrs):
        print(attrs)

        if not attrs.get("phone").lstrip("+").isdigit():
            raise exceptions.ValidationError("Invalid phone number")
        return attrs


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "title"
