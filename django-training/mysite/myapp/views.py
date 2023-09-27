from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import logging

from .forms import ContactForm


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
