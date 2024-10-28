from django.db import models

class Invoice(models.Model):
    invoice_id = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.customer_name}"