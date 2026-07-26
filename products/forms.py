from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            "name",
            "product_code",
            "category",
            "weight",
            "wage_percent",
            "image",
            "description",
            "is_active",
        ]

        labels = {
            "name": "نام محصول",
            "product_code": "کد محصول",
            "category": "دسته‌بندی",
            "weight": "وزن (گرم)",
            "wage_percent": "درصد اجرت",
            "image": "تصویر محصول",
            "description": "توضیحات",
            "is_active": "فعال",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام محصول",
            }),
            "product_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "کد محصول",
            }),
            "category": forms.Select(attrs={
                "class": "form-select",
            }),
            "weight": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.001",
            }),
            "wage_percent": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }

    def clean_weight(self):
        weight = self.cleaned_data["weight"]

        if weight <= 0:
            raise forms.ValidationError("وزن باید بیشتر از صفر باشد.")

        return weight

    def clean_wage_percent(self):
        wage = self.cleaned_data["wage_percent"]

        if wage < 0:
            raise forms.ValidationError("درصد اجرت نمی‌تواند منفی باشد.")

        if wage > 100:
            raise forms.ValidationError("درصد اجرت نمی‌تواند بیشتر از ۱۰۰ باشد.")

        return wage