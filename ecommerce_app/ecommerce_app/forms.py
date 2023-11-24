from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Payment#, Seller

#create class for project form
class ProductForm(ModelForm):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    class Meta:
        model = Product
        fields =('name','price', 'description')


# Create your models here.
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields =('name','card', 'expdate')
