from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    template_name = "products/product_list.html"

    context_object_name = "products"

    paginate_by = 10

    ordering = ["-created_at"]