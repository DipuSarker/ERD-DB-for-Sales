from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OTP(models.Model):
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    
    def __str__(self):
        return self.otp + " - " + self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=266)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='categories')
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=266)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=266)
    img_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=266)
    email = models.EmailField(blank=True, null=True, max_length=266)
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    
    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    payable = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    
class InvoiceProduct(models.Model):
    qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice_products')
    
