from django import forms
from django.forms import ModelForm
from .models import Payment

# Create your models here.
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields =('name','card', 'expdate')
