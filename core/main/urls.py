from django.urls import path
from .views import ItemListAPIVIew, RegisterView, LoginView

urlpatterns = [
    path("item-list", ItemListAPIVIew.as_view(), name="item-list"),
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
]
