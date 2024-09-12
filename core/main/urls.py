from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    BlogListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    BlogRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("categories", CategoryListCreateAPIView.as_view(), name="category-list"),
    path("blogs", BlogListCreateAPIView.as_view(), name="blog-list"),
    path(
        "category/<int:pk>",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-list",
    ),
    path("blog/<int:pk>", BlogRetrieveUpdateDestroyAPIView.as_view(), name="blog-list"),
]
