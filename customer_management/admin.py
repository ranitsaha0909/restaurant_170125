from django.contrib import admin

from customer_management.models import CustomerDetails


# Register your models here.
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number"]

admin.site.register(CustomerDetails, CustomerDetailsAdmin)
