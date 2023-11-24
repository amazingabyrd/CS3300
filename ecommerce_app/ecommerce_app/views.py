from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import ProductForm, PaymentForm
import stripe
from django.conf import settings

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

def index(request):
    products = Product.objects.all()
    return render(request, 'ecommerce_app/index.html', {'products':products})

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            product = form.save()
            # Redirect back to the portfolio detail page or any other page you want
            return redirect('/')  # Change 'products' to the appropriate URL name

    context = {'form': form}
    return render(request, 'ecommerce_app/product_form.html', context)

def updateProduct(request, product_id ):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('product-detail', product.id)
    context = {'form': form}
    return render(request, 'ecommerce_app/product_form.html', context)

def deleteProduct(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {'product': product}
    return render(request, 'ecommerce_app/product_delete.html', context)


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'registration/register.html', context)




def payment(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save
            return redirect('payment_success')
        else:
            return redirect('payment_failed')
    return render(request, 'ecommerce_app/payment_form.html', {'form':form})


def payment_success(request):
    return render(request, 'ecommerce_app/payment_success.html')

def payment_failed(request):
    return render(request, 'ecommerce_app/payment_failure.html')
