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
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=400, default='')
    image = models.ImageField(upload_to='upload/product/')
    display = models.CharField(max_length=50, null=True, blank=True)  
    ram = models.CharField(max_length=50, null=True, blank=True)  
    storage = models.CharField(max_length=50, null=True, blank=True) 
    battery = models.CharField(max_length=50, null=True, blank=True)  
    processor = models.CharField(max_length=100, null=True, blank=True) 
    camera = models.CharField(max_length=100, null=True, blank=True)  
    stock = models.PositiveIntegerField(null=True, blank=True)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    def get_stock_status(self):
        if self.stock is None or self.stock == 0:
            return "Out of Stock"
        elif self.stock < 20:
            return "Limited Stock"
        else:
            return "In Stock"

    def __str__(self):
        return self.name


    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)  
    email = models.EmailField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.name if self.name else "Unnamed Customer"
    
    @classmethod
    def get_total_user(cls):
        total_user = cls.objects.count()
        return total_user


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return f"Order {self.id}"
    
    @staticmethod
    def get_all_order():
        return Order.objects.all()

    @classmethod
    def get_next_transaction_id(cls):

        last_order = cls.objects.order_by('-id').first() 
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

    @classmethod
    def get_total_sales(cls):
        total_sales = sum(order.get_cart_total for order in cls.objects.all())
        return total_sales
    
    @classmethod
    def get_total_orders(cls):
        total_orders = cls.objects.count()
        return total_orders


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        product_name = self.product.name if self.product else 'No Product'
        order_id = self.order.id if self.order else 'No Order'
        return f"{product_name} - {self.quantity} (Order {order_id})"

    @property
    def get_total(self):
        if self.product:
            return self.product.price * self.quantity
        return 0  
    
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

class ContactUs(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.TextField(null=False)

    @classmethod
    def get_all_contacts(cls):
        return cls.objects.all()

    def __str__(self):
        return f"{self.name} ({self.email})"
