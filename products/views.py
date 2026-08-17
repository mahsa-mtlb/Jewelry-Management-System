from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from categories.models import Category
from .forms import ProductForm
from .models import Product


class ProductListView( ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 3
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = Product.objects.all()

        search = self.request.GET.get("search", "")
        category = self.request.GET.get("category", "")
        status = self.request.GET.get("status", "")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(product_code__icontains=search)
            )

        if category:
            queryset = queryset.filter(category_id=category)

        if status == "active":
            queryset = queryset.filter(is_active=True)

        elif status == "inactive":
            queryset = queryset.filter(is_active=False)

        return queryset.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search"] = self.request.GET.get("search", "")
        context["categories"] = Category.objects.all()
        context["selected_category"] = self.request.GET.get("category", "")
        context["selected_status"] = self.request.GET.get("status", "")

        return context


class ProductCreateView(SuccessMessageMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"

    success_url = reverse_lazy("products:list")
    success_message = "محصول با موفقیت ثبت شد."


class ProductUpdateView(SuccessMessageMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"

    success_url = reverse_lazy("products:list")
    success_message = "محصول با موفقیت ویرایش شد."


class ProductDeleteView(
    DeleteView
):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("products:list")


class ProductDetailView(
    DetailView
):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"