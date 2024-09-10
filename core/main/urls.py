from django.urls import path
from .views import WomenAPIView

urlpatterns = [path("", WomenAPIView.as_view(), name="women-list")]
