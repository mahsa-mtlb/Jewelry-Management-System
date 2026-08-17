from django.urls import path

from .views import (
    GoldPriceListView,
    GoldPriceCreateView,
    GoldPriceUpdateView,
)

app_name = "pricing"

urlpatterns = [
    path("", GoldPriceListView.as_view(), name="list"),
    path("create/", GoldPriceCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", GoldPriceUpdateView.as_view(), name="update"),
]