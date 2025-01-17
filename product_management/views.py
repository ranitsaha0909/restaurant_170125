from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views import View

from product_management.models import Products

from product_management.forms import OrderForm


# Create your views here.
class OrderView(View):
    def get(self, request):
        context = {
            "title": "New Order",
            "products": Products.objects.filter(is_active=True),
        }
        return render(request, "order_new.html", context=context)


    def post(self, request):
        form = OrderForm(request.POST)
        order_details= form.save()
        context = {
            "title": "Order Successful",
            "order_details": order_details
        }
        return render(request, "order_success.html", context=context)