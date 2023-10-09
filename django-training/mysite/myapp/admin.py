from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from .models import Product, Category


class ProductInline(admin.TabularInline):
    model = Product


class ProductAdmin(admin.ModelAdmin):
    # fields = ["name", "category", "price", "discount_price", "quantity", "description"]
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
    actions = ["make_published", "export_selected_objects"]

    @admin.action(description="Add more quantity")
    def make_published(self, request, queryset):
        updated = queryset.update(quantity=100)
        self.message_user(
            request,
            ngettext(
                "%d story was successfully to add more quantity",
                "%d stories were successfully to add more quantity",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Delete pages", permissions=["delete"])
    def export_selected_objects(self, request, queryset):
        selected = queryset.values_list("pk", flat=True)
        return HttpResponseRedirect(
            "/delete/?ids=%s"
            % (
                ",".join(str(pk) for pk in selected),
            )
        )


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
