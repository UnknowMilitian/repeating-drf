from rest_framework import serializers
from .models import Category, Women


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = [
            "cat_id",
            "title",
            "content",
            "time_created",
            "time_updated",
            "is_published",
        ]
