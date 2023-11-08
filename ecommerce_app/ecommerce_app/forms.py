from django.forms import ModelForm
from .models import Product

#create class for project form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =('name','price', 'description')
#
# class SignIn()
