from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import *
from .forms import ProductForm


class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

def index(request):
    products = Product.objects.all()
    return render(request, 'ecommerce_app/index.html', {'products':products})

    # Default from template
    # return HttpResponse("Hello, world. You're at the polls index.")

#
# def createProduct(request):
#     form = ProductForm()
#
#     if request.method == 'POST':
#         form = ProductForm()
#             # Save the form without committing to the database
#         product = form.save(commit=False)
#         product.save()
#         # Redirect back to the portfolio detail page
#         return redirect('products')
#
#     context = {'form': form}
#     return render(request, 'ecommerce_app/product_form.html', context)
#
def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            product = form.save()
            # Redirect back to the portfolio detail page or any other page you want
            return redirect('/')  # Change 'products' to the appropriate URL name
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'ecommerce_app/product_form.html', context)

def deleteProduct(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {'product': product}
    return render(request, 'ecommerce_app/product_delete.html', context)



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

