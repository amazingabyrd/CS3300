from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import *


class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

def index(request):
    products = Product.objects.all()
    return render(request, 'ecommerce_app/index.html', {'products':products})

    # Default from template
    # return HttpResponse("Hello, world. You're at the polls index.")


# # Ge05 part 3
# def createProduct(request, portfolio_id):
#     form = ProjectForm()
#     portfolio = Portfolio.objects.get(pk=portfolio_id)
#
#     if request.method == 'POST':
#         # Create a new dictionary with form data and portfolio_id
#         project_data = request.POST.copy()
#         project_data['portfolio_id'] = portfolio_id
#
#         form = ProjectForm(project_data)
#         if form.is_valid():
#             # Save the form without committing to the database
#             project = form.save(commit=False)
#
#             # Set the portfolio relationship
#             project.portfolio = portfolio
#             project.save()
#
#             # Redirect back to the portfolio detail page
#             return redirect('portfolio-detail', portfolio_id)
#
#     context = {'form': form}
#     return render(request, 'portfolio_app/project_form.html', context)
#
#
#
# # Ge05 Delete Project code
# def deleteProduct(request, product_id:
#     project = Project.objects.get(pk=project_id)
#     if request.method == 'POST':
#         project.delete()
#         return redirect('portfolio-detail', portfolio_id)
#     context = {'project': project}
#     return render(request, 'portfolio_app/project_delete.html', context)
#
#
# def updateProduct(request, project_id, portfolio_id ):
#     project = Project.objects.get(pk=project_id)
#     form = ProjectForm(instance=project)
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, instance=project)
#         if form.is_valid():
#             form.save()
#         return redirect('portfolio-detail', portfolio_id)
#     context = {'form': form}
#     return render(request, 'portfolio_app/project_form.html', context)
#
# def updateProduct(request, portfolio_id ):
#     student = Student.objects.get(portfolio=portfolio_id)
#     portfolio = Portfolio.objects.get(pk=portfolio_id)
#     form = PortfolioForm(instance=portfolio)
#     if request.method == 'POST':
#         form = PortfolioForm(request.POST, instance=portfolio)
#         if form.is_valid():
#             form.save()
#         return redirect('student-detail', student.id)
#     context = {'form': form}
#     return render(request, 'portfolio_app/portfolio_form.html', context)

