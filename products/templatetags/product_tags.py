from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter
def toman(value):
    if value is None:
        return "-"

    return f"{intcomma(int(value))} تومان"