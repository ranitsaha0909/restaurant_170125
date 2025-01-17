from django import forms

from product_management.models import Orders

from customer_management.models import CustomerDetails

from product_management.models import Products


class OrderForm(forms.Form):

    def save(self):
        customer_details, _ = CustomerDetails.objects.get_or_create(
            full_name=self.data["full_name"],
            phone_number=self.data["phone_number"],
        )
        products = []
        for key, value in self.data.items():
            if key.startswith("product_") and not key.endswith("quantity"):
                product_quantity = self.data[f"{key}_quantity"]
                product_id = key.replace("product_", "")
                products.append({
                    "id": product_id,
                    "quantity": product_quantity
                })

        order_details = Orders.objects.create(customer=customer_details, is_active=True)
        for product in products:
            order_details.products.add(Products.objects.get(id=product["id"]),
                                       through_defaults={"quantity": product["quantity"]}
                                       )
            # order_details.products.save()

        return order_details
