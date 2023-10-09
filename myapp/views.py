from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm, BlogForm, ProductForm

from .models import Blog, Product


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Welcome to my app.")


def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect("thanks/")

    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def move_to_thanks_page(request):
    return render(request, "thanks.html")


def get_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            form_name = form.cleaned_data["name"]
            form_tag_line = form.cleaned_data["tagline"]
            new_blog = Blog(name=form_name, tagline=form_tag_line)
            new_blog.save()
            return HttpResponseRedirect("thanks/")
    else:
        form = BlogForm()
    return render(request, "blog-form.html", {"form": form})


def get_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            category = form.cleaned_data["category"]
            price = form.cleaned_data["price"]
            discount_price = form.cleaned_data["discount_price"]
            quantity = form.cleaned_data["quantity"]
            description = form.cleaned_data["description"]
            new_product = Product(
                name=name,
                category=category,
                price=price,
                discount_price=discount_price,
                quantity=quantity,
                description=description,
            )
            print("come here")
            new_product.save()
            return HttpResponseRedirect("list-product")
    else:
        form = ProductForm()
    return render(request, "product-form.html", {"form": form})


def get_list_product(request):
    list_product = Product.objects.all()
    return render(request, "list-product.html", {"data": list_product})
