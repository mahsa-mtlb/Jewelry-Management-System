from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "categories/category_list.html",
        {
            "categories": categories,
        },
    )


def category_create(request):

    if request.method == "POST":

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("categories:list")

    else:
        form = CategoryForm()

    print(form)

    return render(
        request,
        "categories/category_form.html",
        {
            "form": form,
        },
    )