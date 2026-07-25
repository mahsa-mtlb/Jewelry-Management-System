from django.contrib import admin
from .models import GoldPrice


@admin.register(GoldPrice)
class GoldPriceAdmin(admin.ModelAdmin):
    list_display = (
        "price_per_gram",
        "updated_at",
    )

    ordering = (
        "-updated_at",
    )