from django.db import models
from django.urls import reverse

# Payment Template form class
class Payment(models.Model):
    name = models.CharField(max_length=200)
    card = models.CharField(max_length=40)
    expdate = models.CharField(max_length=20)
    def __str__(self):
        return self.name
