from django.contrib import admin
from django.utils.html import format_html

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "thumbnail",
        "name",
        "product_code",
        "category",
        "weight",
        "wage_percent",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "product_code",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "preview_image",
    )

    fieldsets = (
        ("اطلاعات محصول", {
            "fields": (
                "name",
                "product_code",
                "category",
                "weight",
                "wage_percent",
                "is_active",
            )
        }),
        ("تصویر", {
            "fields": (
                "image",
                "preview_image",
            )
        }),
        ("توضیحات", {
            "fields": (
                "description",
            )
        }),
        ("اطلاعات سیستم", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    @admin.display(description="تصویر")
    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px; object-fit:cover;" />',
                obj.image.url,
            )
        return "-"

    @admin.display(description="پیش‌نمایش تصویر")
    def preview_image(self, obj):
        if obj.pk and obj.image:
            return format_html(
                '<img src="{}" width="250" style="border-radius:10px;" />',
                obj.image.url,
            )
        return "هنوز تصویری بارگذاری نشده است."