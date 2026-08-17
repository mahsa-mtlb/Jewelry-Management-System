from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import GoldPrice
from .forms import GoldPriceForm


class GoldPriceListView(ListView):
    model = GoldPrice
    template_name = "pricing/goldprice_list.html"
    context_object_name = "prices"
    ordering = ["-created_at"]


class GoldPriceCreateView(SuccessMessageMixin,CreateView):
    model = GoldPrice
    form_class = GoldPriceForm
    template_name = "pricing/goldprice_form.html"

    success_url = reverse_lazy("pricing:list")
    success_message = "قیمت روز با موفقیت ثبت شد."


class GoldPriceUpdateView(SuccessMessageMixin,UpdateView):
    model = GoldPrice
    form_class = GoldPriceForm
    template_name = "pricing/goldprice_form.html"

    success_url = reverse_lazy("pricing:list")
    success_message = "قیمت روز با موفقیت ویرایش شد."