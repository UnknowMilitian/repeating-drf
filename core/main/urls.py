from django.urls import path
from .views import UserDetailView, Login

urlpatterns = [
    path("user/<int:pk>", UserDetailView.as_view(), name="user-detail"),
    path("login", Login.as_view(), name="login"),
]
