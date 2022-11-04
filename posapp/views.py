from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import CustomerForm
from .forms import CategoryForm
from .forms import ProductForm
from .forms import TransactionForm
from .forms import VendorForm
from .forms import SupervisorForm
from .forms import EmployeeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Employee
from .models import Customer
from .models import Category
from .models import Product
from .models import Transaction
from .models import Vendor
from .models import Supervisor
from django.template import loader
from django.urls import reverse
#from posapp.models import Employee

# from POS.models import Departments, Employees
# from POS.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

# Renders html code
# def index(request):
#     return render(request, 'base.html')

# Tylers part below

@login_required(login_url = '/login')

def home(request):
    return render(request, 'home.html')

def EmpHome(request):
    return render(request, 'EmpHome.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

def add_emp(request):
    form = EmployeeForm
    submitted = False

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_emp')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'employee.html', {'form': form, 'submitted': submitted})


def add_customer(request):
    form = CustomerForm
    submitted = False

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_cust')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'customer.html', {'form': form, 'submitted': submitted})



def custLand(request):
    return render(request, 'CustomerReport/CustomerLanding.html')

# def adminEmp(request):
#     return render(request, 'AdminReport/AdminEmployee.html')



def adminVend(request):
    return render(request, 'AdminReport/AdminVendor.html')



def empTrans(request):
    return render(request, 'EmployeeReport/EmployeeTransactions.html')



def custRep(request):
    return render(request, 'EmployeeReport/EmployeeTransactions.html')



def shop(request):
    return render(request, 'shop.html')



def custTrans(request):
    return render(request, 'CustomerReport/CustomerLanding.html')



def empTable(request):
    mydata = Employee.objects.all()
    template = loader.get_template('AdminReport/AdminEmployee.html')
    context = {
        'employees': mydata,
    }
    return HttpResponse(template.render(context, request))



def custTable(request):
    mydata = Customer.objects.all()
    template = loader.get_template('CustomerReport/CustomerLanding.html')
    context = {
        'customers': mydata,
    }
    return HttpResponse(template.render(context, request))



def delete(request, id):
  member = Customer.objects.get(cust_id=id)
  member.delete()
  return HttpResponseRedirect(reverse('custTable'))



def deleteEmp(request, id):
  member = Employee.objects.get(emp_id=id)
  member.delete()
  return HttpResponseRedirect(reverse('empTable'))


def add_product(request):
    form = ProductForm
    submitted = False

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_product')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'product.html', {'form': form, 'submitted': submitted})

def add_supervisor(request):
    form = SupervisorForm
    submitted = False

    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_supervisor')
    else:
        form = SupervisorForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'product.html', {'form': form, 'submitted': submitted})

def add_vendor(request):
    form = VendorForm
    submitted = False

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_vendor')
    else:
        form = VendorForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'vendor.html', {'form': form, 'submitted': submitted})

def add_category(request):
    form = CategoryForm
    submitted = False

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_category')
    else:
        form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'category.html', {'form': form, 'submitted': submitted})

def add_transaction(request):
    form = TransactionForm
    submitted = False

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_transaction')
    else:
        form = TransactionForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'transaction.html', {'form': form, 'submitted': submitted})