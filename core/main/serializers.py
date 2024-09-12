from rest_framework import serializers
from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["title", "post_count"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["category", "title", "body"]
