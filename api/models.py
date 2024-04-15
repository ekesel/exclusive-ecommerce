from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class TimeStamped(models.Model):
    """
    Provides created and updated timestamps on models.
    """

    class Meta:
        abstract = True

    created = models.DateTimeField(null=True, editable=False,)
    updated = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        _now = timezone.now()
        self.updated = _now
        if not self.id:
            self.created = _now
        super(TimeStamped, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class subCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    
class Product(TimeStamped):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=4, null=True, default=Decimal("0"))
    discounted_price = models.DecimalField(max_digits=20, decimal_places=4, null=True, default=Decimal("0"))
    sub_category = models.ForeignKey(subCategory, related_name='prod_sub_categories', on_delete=models.PROTECT)
    product_desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.name
    
class ColorVariation(models.Model):
    availability = models.BooleanField(default=True)
    color_hex =  models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name="product_colors", on_delete=models.PROTECT)

class SizeVariation(models.Model):
    SIZES = (('XS', 'XS'), ('S', 'S'), ('L', 'L'),
              ('M', 'M'), ('XXL', 'XXL'), ('XL', 'XL'))
    availability = models.BooleanField(default=True)
    product = models.ForeignKey(Product, related_name="product_sizes", on_delete=models.PROTECT)
    size = models.CharField(max_length=50, choices=SIZES)

class PincodeProductAvailability(models.Model):
    product = models.ForeignKey(Product, related_name="product_pincodes", on_delete=models.PROTECT)
    pincode = models.CharField(max_length=10)
    avialability = models.BooleanField(default=True)

class ProductImages(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name

class Rating(TimeStamped):
    product = models.ForeignKey(Product, related_name="product_ratings", on_delete=models.PROTECT)
    rating = models.DecimalField(max_digits=20, decimal_places=2, null=True, default=Decimal("0"))
    user = models.ForeignKey(User, related_name='customer_ratings', on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name+' '+ self.user.username
    
class CustomerDetail(TimeStamped):
    user = models.OneToOneField(User, related_name="customer_detail", null=True, blank=True, on_delete=models.PROTECT)
    subscribed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=500)


class Order(TimeStamped):
    STATUS = (('CANCELLED', 'CANCELLED'), ('SHIPPED', 'SHIPPED'), ('PAYMENT_PENDING', 'PAYMENT_PENDING'),
              ('DELIVERED', 'DELIVERED'), ('SUCCESS', 'SUCCESS'))
    DELIVERY_MODE = (('BANK', 'Bank'), ('CASH', 'Cash On Delivery'))
    user = models.ForeignKey(User, related_name='user_orders', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name="product_orders", on_delete=models.PROTECT)
    order_status = models.CharField(max_length=20, choices=STATUS)
    delivery_mode = models.CharField(max_length=50, choices=DELIVERY_MODE)
    size_variation = models.ForeignKey(SizeVariation, related_name="order_size", on_delete=models.PROTECT)
    color_variation = models.ForeignKey(ColorVariation, related_name="order_color", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

class Wishlist(TimeStamped):
    user = models.ForeignKey(User, related_name='user_wishlist', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name="product_wishlist", on_delete=models.PROTECT)
    size_variation = models.ForeignKey(SizeVariation, related_name="size_wishlist", on_delete=models.PROTECT)
    color_variation = models.ForeignKey(ColorVariation, related_name="color_wishlist", on_delete=models.PROTECT)

class Cart(TimeStamped):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name="cart", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

class GiftVoucher(TimeStamped):
    code = models.CharField(max_length=100,unique=True)
    no_times_allowed = models.IntegerField(default=1)
    expiry_date = models.DateTimeField(null=True)

class BillingDetails(TimeStamped):
    user = models.ForeignKey(User, related_name='user_billing_details', on_delete=models.PROTECT)
    order = models.ForeignKey(Order, related_name='order_billing_details', on_delete=models.PROTECT)
    subscribed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=500)
    house_no = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Lead(TimeStamped):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.name