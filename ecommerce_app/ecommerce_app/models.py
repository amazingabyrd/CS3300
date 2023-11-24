from django.db import models
from django.urls import reverse

# Original Class
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500, blank = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

# Payment Template form class
class Payment(models.Model):
    name = models.CharField(max_length=200)
    card = models.CharField(max_length=40)
    expdate = models.CharField(max_length=20)
    def __str__(self):
        return self.name
