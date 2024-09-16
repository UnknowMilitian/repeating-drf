from rest_framework import serializers
from rest_framework import exceptions
from .models import User, Token, Category, Blog


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "phone", "full_name", "is_staff", "is_superuser")


class LoginConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    phone = serializers.CharField(max_length=20)


class PhoneAndPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255)

    def validate_password(self, value):
        if len(value) > 8:
            raise exceptions.ValidationError(
                "Password must be at least 8 characters long"
            )
        return value

    def validate(self, attrs):
        print(attrs)

        if not attrs.get("phone").lstrip("+").isdigit():
            raise exceptions.ValidationError("Invalid phone number")
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["title", "post_count"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["category", "title", "body"]
