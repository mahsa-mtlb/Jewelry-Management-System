from django.db import models

from categories.models import Category

from .services import calculate_final_price


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام محصول"
    )

    product_code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="کد محصول"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="دسته‌بندی"
    )

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        verbose_name="وزن (گرم)"
    )

    wage_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="درصد اجرت"
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="تصویر محصول"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.product_code})"

    @property
    def final_price(self):
        return calculate_final_price(self)
