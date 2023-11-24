from django.shortcuts import render
from .forms import PaymentForm
# Payments extras
import stripe
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from django.http import JsonResponse
from django.conf import settings

###########################################################################################
# Payments
stripe.api_key = settings.STRIPE_SECRET_KEY
#
# def payment(request):
#     form = PaymentForm()
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             payment = form.save
#             return redirect('/')
#     return render(request, 'ecommerce_app/payment_form.html', {'form':form})
#
#
# def payment_success(request):
#     return render(request, 'ecommerce_app/payment_success.html')
#
# def payment_failed(request):
#     return render(request, 'ecommerce_app/payment_failure.html')
