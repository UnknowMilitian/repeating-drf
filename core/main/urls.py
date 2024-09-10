from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WomenAPIList, WomenAPIUpdate, WomenAPIDeleteView

# router = DefaultRouter()
# router.register(r"women", WomenViewSet)

# urlpatterns = [path("", include(router.urls))]

urlpatterns = [
    path("women/", WomenAPIList.as_view(), name="women-list"),
    path("women-detail/<int:pk>", WomenAPIUpdate.as_view(), name="women-detail"),
    path("women-delete/<int:pk>", WomenAPIDeleteView.as_view(), name="women-delete"),
]
