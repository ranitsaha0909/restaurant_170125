from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = "CustomerDetail"
        verbose_name_plural = "CustomerDetails"

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"