from django import forms

from .models import GoldPrice


class GoldPriceForm(forms.ModelForm):
    class Meta:
        model = GoldPrice

        fields = [
            "price_per_gram",
            "profit_percent",
        ]

        labels = {
            "price_per_gram": "قیمت هر گرم طلا",
            "profit_percent": "درصد سود",
        }

        widgets = {
            "price_per_gram": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "قیمت هر گرم طلا",
                }
            ),
            "profit_percent": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "درصد سود",
                    "step": "0.01",
                }
            ),
        }
        