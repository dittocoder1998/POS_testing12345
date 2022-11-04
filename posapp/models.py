from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField('Employee ID', max_length = 3)
    emp_name = models.CharField('Employee Name', max_length = 50)
    emp_pay_rate = models.CharField('Pay Rate', max_length = 6)
    emp_weekly_hours = models.DecimalField('Weekly Hours', max_digits = 3, decimal_places = 1)
    emp_start_date = models.DateField('Employee Start Date')
    emp_dob = models.DateField('Date of Birth')
    emp_email = models.EmailField('Email Address')


class Customer(models.Model):
    cust_id = models.CharField('Customer ID', max_length = 3)
    cust_name = models.CharField('Customer Name', max_length = 50)
    cust_email = models.EmailField('Email Address')
    cust_dob = models.DateField("Customer's Date of Birth")

class Supervisor(models.Model):
    supervisor_id = models.CharField('Supervisor ID', max_length = 3)
    supervisor_name = models.CharField('Supervisor Name', max_length = 20)

class Vendor(models.Model):
    vendor_id = models.CharField('Vendor ID', max_length = 3)
    vendor_name = models.CharField('Vendor name', max_length = 50)
    location = models.CharField('Location', max_length = 50)
    order_status = models.CharField('order status', max_length = 20)

class Category(models.Model):
    category_id = models.CharField('Category ID', max_length = 3)
    category_name = models.CharField('Category ID', max_length = 3)

class Transaction(models.Model):
    transaction_id = models.CharField('Transaction ID', max_length = 3)
    customer_id = models.CharField('Customer ID', max_length = 3)
    product_id = models.CharField('Product ID', max_length = 3)
    price = models.CharField('Price', max_length = 6)
    employee_id = models.CharField('Employee ID', max_length = 3)
    emp_name = models.CharField('Employee name', max_length = 20)
    customer_name = models.CharField('Customer name', max_length = 3)
    time_of_transaction = models.DateField('Time of transaction')

class Product(models.Model):
    product_id = models.CharField('Product ID', max_length = 3)
    product_name = models.CharField('Product name', max_length = 20)
    price = models.DecimalField('Price' , max_digits = 5,decimal_places = 2)
    vendor_id = models.CharField('Product name', max_length = 20)
    vendor_category = models.CharField('Vendorcategory', max_length = 50)
    prod_amount = models.CharField('Prod amount', max_length = 6)
    in_stock = models.BooleanField('in_stock')