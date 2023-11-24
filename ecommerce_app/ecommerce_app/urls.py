from django.urls import path, include
from . import views

urlpatterns = [

    # Default
    path('', views.index, name='index'),

    # # List
    # path('products/', views.ProductListView.as_view(), name='products'),

    # Details url, view, and name to call from view
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


#Create Product
    path('product/create_product/', views.createProduct, name='create_product'),


#Delete Product
    path('product/<int:product_id>/delete_product', views.deleteProduct, name='delete_product'),

# #Update Product
    path('product/<int:product_id>/update_product', views.updateProduct, name='update_product'),


    # register user account
    path('accounts/register', views.registerPage, name="register"),

    # # Payments
    path('payment/', views.payment, name='payment'),
    path('payment_success', views.payment_success, name='payment_success'),
    path('payment_failed', views.payment_failed, name='payment_failed'),


]




