from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "title", "description", "image", "resized_image"]


# Registration Serializers
class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        label="Confirm password",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password do not much")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
