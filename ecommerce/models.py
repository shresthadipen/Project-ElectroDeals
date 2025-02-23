from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='upload/brand', null=True, blank=True)

    @staticmethod
    def get_all_brand():
        return Brand.objects.all()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='upload/category', default='')

    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length = 200, default = '')
    image = models.ImageField(upload_to='upload/product/')

    @staticmethod
    def get_all_product():
        return Product.objects.all()
    
    def __str__(self):
        return self.name
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)  
    email = models.EmailField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.name if self.name else "Unnamed Customer"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return f"Order {self.id}"

    @classmethod
    def get_next_transaction_id(cls):
        """
        Generate the next transaction ID, starting from 10000.
        """
        last_order = cls.objects.order_by('-id').first()  # Get the most recent order
        if last_order and last_order.transaction_id:
            try:
                return str(int(last_order.transaction_id) + 1)
            except ValueError:
                return '10000'
        else:
            return '10000'

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = Order.get_next_transaction_id() 
        super(Order, self).save(*args, **kwargs)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} (Order {self.order.id})"

    @property
    def get_total(self):
        return self.product.price * self.quantity
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False, blank=True, verbose_name="Street Address")
    city = models.CharField(max_length=200, null=False, blank=True)
    state = models.CharField(max_length=200, null=False, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zipcode}"
