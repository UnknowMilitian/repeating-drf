from rest_framework import serializers
from .models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["category", "title", "body"]
