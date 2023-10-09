from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from myapp.models import Blog, Product


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["name", "tagline"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "price",
            "discount_price",
            "quantity",
            "description",
        ]

    def clean_recipients(self):
        data = self.cleaned_data["name"]
        if not data:
            raise ValidationError("Please enter the Product name!")
        return data
