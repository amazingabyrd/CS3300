from django.urls import path
from . import views

urlpatterns = [

    # Default
    path('', views.index, name='index'),

    # List
    path('products/', views.ProductListView.as_view(), name='products'),

    # Details url, view, and name to call from view
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

]



