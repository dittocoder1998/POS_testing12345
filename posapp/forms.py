from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Employee, Customer,Supervisor,Category,Product,Transaction,Vendor

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_id': '',
            'emp_name': '',
            'emp_pay_rate': '',
            'emp_weekly_hours': '',
            'emp_start_date': '',
            'emp_dob': '',
            'emp_email': '',
        }

        widgets = {
            'emp_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}),
            'emp_pay_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pay Rate'}),
            'emp_weekly_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weekly Hours'}),
            'emp_start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            'emp_dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'emp_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'cust_id': '',
            'cust_name': '',
            'cust_email': '',
            'cust_dob': '',
         }

        widgets = {
            'cust_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer ID'}),
            'cust_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'cust_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'cust_dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
         }

class SupervisorForm(ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'
        labels = {
            'supervisor_id': '',
            'supervisor_name': '',
         }

        widgets = {
            'supervisor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor ID'}),
            'supervisor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supervisor Name'}),
         }


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        labels = {
            'vendor_id': '',
            'vendor_name': '',
            'location': '',
            'order_status': '',
         }

        widgets = {
            'vendor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor ID'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'order_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order Status'}),
         }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'category_id': '',
            'category_name': '',
         }

        widgets = {
            'category_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category ID'}),
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
         }


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        labels = {
            'transaction_id': '',
            'customer_id': '',
            'product_id': '',
            'price': '',
            'employee_id': '',
            'emp_name':  '',
            'customer_name':  '',
            'time_of_transaction':  '',
         }

        widgets = {
            'transaction_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transaction ID'}),
            'customer_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer ID'}),
            'product_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product ID'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee name'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer name'}),
            'time_of_transaction':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Time of transaction'}),
         }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': '',
            'product_name': '',
            'price': '',
            'vendor_id': '',
            'vendor_category': '',
            'prod_amount': '',
            'in_stock': '',
         }

        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product ID'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'vendor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor ID'}),
            'vendor_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Category'}),
            'prod_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Amount'}),
            'in_stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'in_stock'}),
         }