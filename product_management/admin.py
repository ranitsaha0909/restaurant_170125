from django.contrib import admin

from product_management.models import Products, Orders, ProductOrderQuantity


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "is_active", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = [
        "category",
        "is_active",
    ]


admin.site.register(Products, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "is_active", "timestamp"]
    list_filter = ["is_active"]

admin.site.register(Orders, OrderAdmin)


class ProductOrderQuantityAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity"]

admin.site.register(ProductOrderQuantity, ProductOrderQuantityAdmin)