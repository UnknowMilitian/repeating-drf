from django.urls import path
from .views import WomenAPIList, WomenAPIUpdate, WomenAPIDetailView

urlpatterns = [
    path(
        "",
        WomenAPIList.as_view(),
        name="women-list",
    ),
    path("women-detail/<int:pk>", WomenAPIUpdate.as_view(), name="women-detail"),
    path("women-change/<int:pk>", WomenAPIDetailView.as_view(), name="women-change"),
]
