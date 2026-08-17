from django.views.generic import TemplateView

from products.models import Product
from categories.models import Category
from pricing.models import GoldPrice


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["product_count"] = Product.objects.count()
        context["category_count"] = Category.objects.count()
        context["active_count"] = Product.objects.filter(is_active=True).count()
        context["inactive_count"] = Product.objects.filter(is_active=False).count()

        context["gold_price"] = (
            GoldPrice.objects.order_by("-created_at").first()
        )

        return context