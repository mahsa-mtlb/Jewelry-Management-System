from decimal import Decimal

from pricing.models import GoldPrice


def calculate_final_price(product):
    """
    محاسبه قیمت نهایی محصول
    فرمول:
    (قیمت روز طلا + درصد اجرت + درصد سود) × وزن
    """

    latest_price = GoldPrice.objects.order_by("-created_at").first()

    if latest_price is None:
        return Decimal("0")

    gold_price = latest_price.price_per_gram
    profit_percent = latest_price.profit_percent
    wage_percent = product.wage_percent

    price_per_gram = (
        gold_price
        + (gold_price * wage_percent / Decimal("100"))
        + (gold_price * profit_percent / Decimal("100"))
    )

    final_price = price_per_gram * product.weight

    return final_price.quantize(Decimal("1"))