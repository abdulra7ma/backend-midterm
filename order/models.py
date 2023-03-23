from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)