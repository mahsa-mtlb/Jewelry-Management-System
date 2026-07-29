from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ProductForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from .models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    template_name = "products/product_list.html"

    context_object_name = "products"

    paginate_by = 10

    ordering = ["-created_at"]

class ProductCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"

    success_url = reverse_lazy("products:list")

    success_message = "محصول با موفقیت ثبت شد."


class ProductUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"

    success_url = reverse_lazy("products:list")

    success_message = "محصول با موفقیت ویرایش شد."

class ProductDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("products:list")
    success_message = "محصول با موفقیت حذف شد."

class ProductDetailView(
    LoginRequiredMixin,
    DetailView,
):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"