from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "category", "price", "discount_price", "quantity", "description"]
    empty_value_display = "No value"
    fieldsets = [
        (
            "Required fields",
            {
                "fields": ["name", "category", "price", "discount_price", "quantity"],
            },
        ),
        (
            "Optional fields",
            {
                "fields": ["description"],
            },
        ),
    ]
    list_display = ["name", "category", "price", "discount_price", "quantity"]
    list_display_links = ["name", "category"]
    # list_editable = ["name"]
    list_filter = ["price", "discount_price", "quantity"]
    list_per_page = 10
    ordering = ["name", "category", "quantity"]
    # radio_fields = {"category": admin.VERTICAL}
    # autocomplete_fields = ["category"]


admin.site.register(Product, ProductAdmin)
