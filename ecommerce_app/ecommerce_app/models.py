from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500, blank = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])



# class Seller(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField("UCCS Email", max_length=200)
    # def __str__(self):
    #     return self.name
    # # Allows seeing the instance of Seller
    # def get_absolute_url(self):
    #     return reverse('seller-detail', args=[str(self.id)])

