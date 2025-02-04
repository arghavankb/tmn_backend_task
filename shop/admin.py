from django.contrib import admin
from . import models


# Filtering products by their price
class PriceFileter(admin.SimpleListFilter):
    title = "price"
    parameter_name = "price"

    def lookups(self, request, model_admin):
        return [
            ("0-500000", "0 - 500,000"),
            ("500000-1000000", "500,000 - 1,000,000"),
            ("1000000-2000000", "1,000,000 - 2,000,000"),
            ("2000000-3000000", "2,000,000 - 3,000,000"),
            ("3000000+", "More than 3,000,000"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "0-500000":
            return queryset.filter(price__gte=0, price__lt=500000)
        elif self.value() == "500000-1000000":
            return queryset.filter(price__gte=500000, price__lt=1000000)
        elif self.value() == "1000000-2000000":
            return queryset.filter(price__gte=1000000, price__lt=2000000)
        elif self.value() == "2000000-3000000":
            return queryset.filter(price__gte=2000000, price__lt=3000000)
        elif self.value() == "3000000+":
            return queryset.filter(price__gte=3000000)
        return queryset


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","price", "description"]
    search_fields = ["title"]
    list_filter = [PriceFileter]
    inlines = [ProductImageInline]
    list_per_page = 10

