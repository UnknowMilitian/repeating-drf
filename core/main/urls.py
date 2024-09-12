from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryRetrieveAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    BlogListCreateAPIView,
    BlogRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("category-list", CategoryListAPIView.as_view(), name="category-list"),
    path("category-create", CategoryCreateAPIView.as_view(), name="category-create"),
    path(
        "category-detail/<int:pk>",
        CategoryRetrieveAPIView.as_view(),
        name="category-detail",
    ),
    path(
        "category-update/<int:pk>",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-update",
    ),
    path("blogs", BlogListCreateAPIView.as_view(), name="blog-list"),
    path("blog/<int:pk>", BlogRetrieveUpdateDestroyAPIView.as_view(), name="blog-list"),
]
