from django.urls import path
from .views import ItemListAPIView

urlpatterns = [path("item-list", ItemListAPIView.as_view(), name="item-list")]
