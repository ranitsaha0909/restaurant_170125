from uuid import uuid4

from django.db import models

from customer_management.models import CustomerDetails


# Create your models here.
class Products(models.Model):
    CATEGORY_CHOICES = (
        (1, "Non-Veg"),
        (2, "Veg"),
        (3, "Dessert"),
    )
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    price = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"


class Orders(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Products, through="ProductOrderQuantity")
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.customer} - {self.timestamp} - {self.id}"


class ProductOrderQuantity(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
