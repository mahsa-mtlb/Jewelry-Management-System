from django.db import models


class GoldPrice(models.Model):
    price_per_gram = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        verbose_name="قیمت هر گرم طلا"
    )

    profit_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=7,
        verbose_name="درصد سود"
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
        verbose_name = "قیمت روز طلا"
        verbose_name_plural = "قیمت روز طلا"

    def __str__(self):
        return f"{self.price_per_gram:,} تومان"